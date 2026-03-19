-- coaching_chatbot/database/migrations.sql

CREATE TABLE IF NOT EXISTS conversation_messages (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id TEXT NOT NULL,
    role TEXT NOT NULL,
    content TEXT NOT NULL,
    intent TEXT,
    timestamp TIMESTAMP DEFAULT NOW(),
    session_id TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS user_memory_chunks (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id TEXT NOT NULL,
    content TEXT NOT NULL,
    embedding vector(3072),
    category TEXT,
    importance FLOAT DEFAULT 0.5,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS user_context_cache (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id TEXT NOT NULL UNIQUE,
    workout_plan JSONB,
    dietary_plan JSONB,
    form_feedback JSONB,
    last_updated TIMESTAMP DEFAULT NOW()
);
