<!-- coaching_chatbot/README.md -->
# PulseAI — Coaching Chatbot Module

Standalone FastAPI microservice that provides conversational coaching to fitness users. Detects 9 intent types, maintains persistent long-term memory using pgvector, receives context from other modules, and returns plan change requests when injuries or adjustments are detected.

## What this module does
- Receives user messages and detects intent (injury / soreness / motivation / plan question / plan adjustment / fitness question / health question / progress update / general)
- Retrieves relevant long-term memories for context
- Streams Gemini 2.5 Flash responses
- Automatically extracts and stores important facts from every conversation
- Returns plan_change_request when plan modifications are needed so other modules can act on them

## API Reference

**POST `/api/chat/message`**
Streaming endpoint. Returns text/plain stream.
Body: `{user_id, session_id, message, exercise_hint?}`

**POST `/api/chat/message/full`**
Non-streaming. Returns full ChatResponse JSON including intent, memories_used, plan_change_request.
Body: `{user_id, session_id, message, exercise_hint?}`

**POST `/api/chat/context`**
Inject workout/dietary/form context for a user. Other modules call this when plans are updated.
Body: `{user_id, workout_plan?, dietary_plan?, form_feedback?}`

**GET `/api/chat/history?user_id=X&session_id=Y`**
Returns conversation history for a session.

**DELETE `/api/chat/history?user_id=X&session_id=Y`**
Clears session history. Memories are NOT deleted.

## How the main backend integrates this module

**Step 1 — Inject context when plans are generated:**
```python
requests.post(
    f"{CHATBOT_URL}/api/chat/context",
    json={
        "user_id": user_id,
        "workout_plan": workout_plan,
        "dietary_plan": dietary_plan
    }
)
```

**Step 2 — Forward user messages for streaming:**
```python
response = requests.post(
    f"{CHATBOT_URL}/api/chat/message",
    json={
        "user_id": user_id,
        "session_id": session_id,
        "message": user_message
    },
    stream=True
)
for chunk in response.iter_content(chunk_size=None):
    yield chunk.decode()
```

**Step 3 — Check for plan change requests:**
```python
response = requests.post(
    f"{CHATBOT_URL}/api/chat/message/full",
    json={...}
)
data = response.json()
if data["plan_change_request"]:
    # forward to workout or dietary module
    pass
```

## How the Next.js frontend integrates

The frontend calls the main backend.
The main backend calls this module.
The frontend never calls this module directly.

Frontend sends: POST `/api/chat` with message
Main backend forwards to this module
Main backend streams response back to frontend

## Memory system explained

Every conversation is analyzed after completion.
Important facts are extracted and stored as vector embeddings in Supabase pgvector.
On the next conversation, the 8 most relevant memories are retrieved and injected into context.
The coach always remembers:
- All injuries ever reported
- Exercise preferences and dislikes
- Motivational patterns
- Goals and progress milestones
- Soreness and recovery patterns

## Local Setup
1. Create Supabase project at supabase.com
2. Run migrations.sql in Supabase SQL editor
3. Get Gemini API key at aistudio.google.com
4. `cd coaching_chatbot`
5. `cp .env.example .env` and fill values
6. `pip install -r requirements.txt`
7. `uvicorn main:app --reload --port 8002`
8. Module runs at http://localhost:8002
9. Docs at http://localhost:8002/docs

## Deployment on Render (free)
1. Push folder to GitHub
2. Render > New Web Service > Connect repo
3. Root directory: coaching_chatbot
4. Build: `pip install -r requirements.txt`
5. Start: `uvicorn main:app --host 0.0.0.0 --port 10000`
6. Add `GEMINI_API_KEY` and `DATABASE_URL`
7. Share the Render URL with your team
