# coaching_chatbot/agent/context_builder.py
from memory.retriever import (
    retrieve_memories,
    retrieve_all_injuries,
    retrieve_preferences,
    get_context_cache
)
from config.settings import MAX_HISTORY_MESSAGES
import json

def get_conversation_history(user_id: str, session_id: str, db) -> list[dict]:
    with db.cursor() as cur:
        cur.execute("""
            SELECT role, content, timestamp, intent
            FROM conversation_messages
            WHERE user_id = %s AND session_id = %s
            ORDER BY timestamp ASC
            LIMIT %s
        """, (user_id, session_id, MAX_HISTORY_MESSAGES))
        
        columns = [desc[0] for desc in cur.description]
        return [dict(zip(columns, row)) for row in cur.fetchall()]

def format_history(messages: list[dict]) -> str:
    lines = []
    for msg in messages:
        if msg["role"] == "user":
            lines.append(f"User: {msg['content']}")
        elif msg["role"] == "assistant":
            lines.append(f"Coach: {msg['content']}")
    return "\n".join(lines)

def build_context(user_id: str, session_id: str, message: str, intent: str, db) -> str:
    history_msgs = get_conversation_history(user_id, session_id, db)
    formatted_history = format_history(history_msgs)
    
    memories = retrieve_memories(user_id, message, db)
    injuries = retrieve_all_injuries(user_id, db)
    preferences = retrieve_preferences(user_id, db)
    cache = get_context_cache(user_id, db)
    
    memories_str = "\n".join(memories) if memories else "No relevant memories found"
    injuries_str = "\n".join(injuries) if injuries else "No injuries on record"
    preferences_str = "\n".join(preferences) if preferences else "No preferences recorded yet"
    
    workout_str = json.dumps(cache["workout_plan"], indent=2) if cache["workout_plan"] else "No workout plan loaded yet"
    dietary_str = json.dumps(cache["dietary_plan"], indent=2) if cache["dietary_plan"] else "No dietary plan loaded yet"
    form_str = json.dumps(cache["form_feedback"], indent=2) if cache["form_feedback"] else "No form feedback available yet"
    
    context = f"""=== CONVERSATION HISTORY ===
{formatted_history}

=== USER LONG-TERM MEMORY ===
The following are important facts remembered
about this user from previous sessions:
{memories_str}

=== USER INJURIES AND PHYSICAL LIMITATIONS ===
Always consider these when giving advice:
{injuries_str}

=== USER PREFERENCES ===
{preferences_str}

=== CURRENT WORKOUT PLAN ===
{workout_str}

=== CURRENT DIETARY PLAN ===
{dietary_str}

=== LATEST FORM FEEDBACK ===
{form_str}

=== CURRENT MESSAGE INTENT ===
Detected intent: {intent}"""

    return context
