# coaching_chatbot/agent/orchestrator.py
from typing import AsyncGenerator
from config.settings import openai_client, MODEL
from agent.safety_guard import check_safety
from agent.intent_detector import detect_intent
from agent.context_builder import build_context
from agent.prompt_builder import build_prompt, SYSTEM_PROMPT
from memory.store import save_memories
from memory.retriever import retrieve_memories
from utils.memory_extractor import extract_memories
from models.schemas import Intent, PlanChangeRequest, ChatResponse
import re


def save_message(user_id, session_id, role, content, intent, db) -> None:
    with db.cursor() as cur:
        cur.execute("""
            INSERT INTO conversation_messages
            (user_id, session_id, role, content, intent, timestamp)
            VALUES (%s, %s, %s, %s, %s, NOW())
        """, (user_id, session_id, role, content, intent))
        db.commit()


def parse_plan_change(response_text: str) -> PlanChangeRequest | None:
    match = re.search(r"PLAN_CHANGE:\s*(.+?)\|(.+?)\|(.+)", response_text)
    if match:
        type_str, reason_str, module_str = match.groups()
        reason_lower = reason_str.lower()
        if "injury" in reason_lower:
            urgency = "immediate"
        elif "soreness" in reason_lower:
            urgency = "next_session"
        else:
            urgency = "this_week"

        return PlanChangeRequest(
            change_type=type_str.strip(),
            reason=reason_str.strip(),
            affected_module=module_str.strip(),
            suggested_modification=reason_str.strip(),
            urgency=urgency,
        )
    return None


async def run(user_id: str, session_id: str, message: str, db) -> ChatResponse:
    safety = check_safety(message)
    if not safety["safe"]:
        save_message(user_id, session_id, "user", message, "general_conversation", db)
        save_message(user_id, session_id, "assistant", safety["response"], None, db)
        return ChatResponse(
            user_id=user_id,
            session_id=session_id,
            response=safety["response"],
            intent_detected=Intent.general_conversation,
            memories_used=[],
            plan_change_request=None,
            new_memories_stored=0,
        )

    intent = detect_intent(message)
    save_message(user_id, session_id, "user", message, intent.value, db)

    context = build_context(user_id, session_id, message, intent.value, db)
    prompt = build_prompt(message, intent.value, context)

    response = openai_client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
    )
    full_response = response.choices[0].message.content.strip()

    plan_change = parse_plan_change(full_response)
    if plan_change:
        full_response = re.sub(r"PLAN_CHANGE:\s*(.+?)\|(.+?)\|(.+)", "", full_response).strip()

    save_message(user_id, session_id, "assistant", full_response, None, db)

    memories_to_store = extract_memories(message, full_response, intent.value)
    count = save_memories(user_id, memories_to_store, db)

    memories_used = retrieve_memories(user_id, message, db)

    return ChatResponse(
        user_id=user_id,
        session_id=session_id,
        response=full_response,
        intent_detected=intent,
        memories_used=memories_used,
        plan_change_request=plan_change,
        new_memories_stored=count,
    )


async def stream_response(user_id: str, session_id: str, message: str, db) -> AsyncGenerator[str, None]:
    safety = check_safety(message)
    if not safety["safe"]:
        save_message(user_id, session_id, "user", message, "general_conversation", db)
        save_message(user_id, session_id, "assistant", safety["response"], None, db)
        yield safety["response"]
        return

    intent = detect_intent(message)
    save_message(user_id, session_id, "user", message, intent.value, db)

    context = build_context(user_id, session_id, message, intent.value, db)
    prompt = build_prompt(message, intent.value, context)

    full_response = ""
    try:
        stream = openai_client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt},
            ],
            temperature=0.7,
            stream=True,
        )
        for chunk in stream:
            delta = chunk.choices[0].delta.content
            if delta:
                full_response += delta
                yield delta
    except Exception as e:
        error_msg = f"\n\n[System Error during generation]: {str(e)}"
        full_response += error_msg
        yield error_msg

    plan_change = parse_plan_change(full_response)
    if plan_change:
        full_response = re.sub(r"PLAN_CHANGE:\s*(.+?)\|(.+?)\|(.+)", "", full_response).strip()

    save_message(user_id, session_id, "assistant", full_response, None, db)

    try:
        memories_to_store = extract_memories(message, full_response, intent.value)
        save_memories(user_id, memories_to_store, db)
    except Exception as e:
        print(f"Memory extraction failed in background: {e}")
