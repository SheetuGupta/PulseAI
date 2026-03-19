# coaching_chatbot/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.chat import router
import os

app = FastAPI(
    title="PulseAI Coaching Chatbot Module",
    description="Conversational coaching agent with persistent memory, intent detection, and plan change requests",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "module": "coaching_chatbot",
        "model": "gemini-2.5-flash",
        "memory": "pgvector",
        "intents_supported": 9
    }

@app.get("/")
def read_root():
    return {
        "module": "PulseAI Coaching Chatbot",
        "endpoints": {
            "stream": "POST /api/chat/message",
            "full": "POST /api/chat/message/full",
            "context": "POST /api/chat/context",
            "history": "GET /api/chat/history",
            "clear": "DELETE /api/chat/history"
        },
        "docs": "/docs"
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8002))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
