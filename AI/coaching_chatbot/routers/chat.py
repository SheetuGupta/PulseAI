# coaching_chatbot/routers/chat.py
from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from models.schemas import (
    ChatRequest, ChatResponse,
    ContextInjectRequest, HistoryResponse
)
from agent.orchestrator import run, stream_response
from memory.store import save_context
from database.connection import get_db

router = APIRouter(prefix="/api/chat", tags=["chat"])

@router.post("/message")
async def process_message_stream(request: ChatRequest, db=Depends(get_db)):
    async def generate():
        async for chunk in stream_response(
            request.user_id,
            request.session_id,
            request.message,
            db
        ):
            yield chunk

    return StreamingResponse(
        generate(),
        media_type="text/plain"
    )

@router.post("/message/full", response_model=ChatResponse)
async def process_message_full(request: ChatRequest, db=Depends(get_db)):
    response = await run(
        request.user_id,
        request.session_id,
        request.message,
        db
    )
    return response

@router.post("/context")
async def inject_context(request: ContextInjectRequest, db=Depends(get_db)):
    save_context(
        request.user_id,
        request.workout_plan,
        request.dietary_plan,
        request.form_feedback,
        db
    )
    return {"success": True, "message": "Context updated"}

@router.get("/history", response_model=HistoryResponse)
async def get_history(user_id: str, session_id: str, limit: int = 20, db=Depends(get_db)):
    with db.cursor() as cur:
        cur.execute("""
            SELECT role, content, timestamp, intent
            FROM conversation_messages
            WHERE user_id = %s AND session_id = %s
            ORDER BY timestamp ASC
            LIMIT %s
        """, (user_id, session_id, limit))
        
        columns = [desc[0] for desc in cur.description]
        messages = [dict(zip(columns, row)) for row in cur.fetchall()]
        
    return HistoryResponse(
        user_id=user_id,
        session_id=session_id,
        messages=messages,
        total_count=len(messages)
    )

@router.delete("/history")
async def clear_history(user_id: str, session_id: str, db=Depends(get_db)):
    with db.cursor() as cur:
        cur.execute("""
            DELETE FROM conversation_messages
            WHERE user_id = %s AND session_id = %s
        """, (user_id, session_id))
        count = cur.rowcount
        db.commit()
    return {"success": True, "deleted": count}
