# coaching_chatbot/memory/store.py
from memory.embedder import embed
from models.schemas import MemoryChunk
import json

def save_memory(user_id: str, content: str, category: str, importance: float, db) -> None:
    vector = embed(content)
    
    with db.cursor() as cur:
        cur.execute("""
            SELECT id, 1 - (embedding <=> %s::vector) as similarity
            FROM user_memory_chunks
            WHERE user_id = %s
            ORDER BY embedding <=> %s::vector
            LIMIT 1
        """, (vector, user_id, vector))
        
        row = cur.fetchone()
        if row and row[1] > 0.92:
            cur.execute("""
                UPDATE user_memory_chunks
                SET content = %s, updated_at = NOW()
                WHERE id = %s
            """, (content, row[0]))
            db.commit()
            return

        cur.execute("""
            INSERT INTO user_memory_chunks
            (user_id, content, embedding, category, importance)
            VALUES (%s, %s, %s, %s, %s)
        """, (user_id, content, vector, category, importance))
        db.commit()

def save_memories(user_id: str, memories: list[MemoryChunk], db) -> int:
    count = 0
    for memory in memories:
        save_memory(user_id, memory.content, memory.category, memory.importance, db)
        count += 1
    return count

def save_context(
    user_id: str,
    workout_plan: dict | None,
    dietary_plan: dict | None,
    form_feedback: dict | None,
    db
) -> None:
    with db.cursor() as cur:
        cur.execute("""
            INSERT INTO user_context_cache 
            (user_id, workout_plan, dietary_plan, form_feedback, last_updated)
            VALUES (%s, %s, %s, %s, NOW())
            ON CONFLICT (user_id) DO UPDATE SET
            workout_plan = COALESCE(EXCLUDED.workout_plan, user_context_cache.workout_plan),
            dietary_plan = COALESCE(EXCLUDED.dietary_plan, user_context_cache.dietary_plan),
            form_feedback = COALESCE(EXCLUDED.form_feedback, user_context_cache.form_feedback),
            last_updated = NOW()
        """, (
            user_id, 
            json.dumps(workout_plan) if workout_plan else None,
            json.dumps(dietary_plan) if dietary_plan else None,
            json.dumps(form_feedback) if form_feedback else None
        ))
        db.commit()
