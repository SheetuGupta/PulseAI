# coaching_chatbot/memory/retriever.py
from memory.embedder import embed
from config.settings import MAX_MEMORY_CHUNKS, MEMORY_IMPORTANCE_THRESHOLD

def retrieve_memories(user_id: str, query: str, db, category_filter: str | None = None) -> list[str]:
    query_vector = embed(query)
    
    with db.cursor() as cur:
        if category_filter:
            cur.execute("""
                SELECT content, importance, 
                1 - (embedding <=> %s::vector) as similarity
                FROM user_memory_chunks
                WHERE user_id = %s AND category = %s
                ORDER BY embedding <=> %s::vector
                LIMIT %s
            """, (query_vector, user_id, category_filter, query_vector, MAX_MEMORY_CHUNKS))
        else:
            cur.execute("""
                SELECT content, importance, 
                1 - (embedding <=> %s::vector) as similarity
                FROM user_memory_chunks
                WHERE user_id = %s
                ORDER BY embedding <=> %s::vector
                LIMIT %s
            """, (query_vector, user_id, query_vector, MAX_MEMORY_CHUNKS))
            
        rows = cur.fetchall()
        
    results = []
    for row in rows:
        content, importance, similarity = row
        if similarity > MEMORY_IMPORTANCE_THRESHOLD:
            results.append({
                "content": content,
                "score": importance * similarity
            })
            
    results.sort(key=lambda x: x["score"], reverse=True)
    return [r["content"] for r in results]

def retrieve_all_injuries(user_id: str, db) -> list[str]:
    with db.cursor() as cur:
        cur.execute("""
            SELECT content FROM user_memory_chunks
            WHERE user_id = %s AND category = 'injury'
            ORDER BY importance DESC, created_at DESC
            LIMIT 10
        """, (user_id,))
        return [row[0] for row in cur.fetchall()]

def retrieve_preferences(user_id: str, db) -> list[str]:
    with db.cursor() as cur:
        cur.execute("""
            SELECT content FROM user_memory_chunks
            WHERE user_id = %s AND category IN ('preference', 'motivation')
            ORDER BY importance DESC
            LIMIT 10
        """, (user_id,))
        return [row[0] for row in cur.fetchall()]

def get_context_cache(user_id: str, db) -> dict:
    with db.cursor() as cur:
        cur.execute("""
            SELECT workout_plan, dietary_plan, form_feedback
            FROM user_context_cache
            WHERE user_id = %s
        """, (user_id,))
        row = cur.fetchone()
        
    if not row:
        return {
            "workout_plan": None,
            "dietary_plan": None,
            "form_feedback": None
        }
        
    return {
        "workout_plan": row[0],
        "dietary_plan": row[1],
        "form_feedback": row[2]
    }
