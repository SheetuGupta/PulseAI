# coaching_chatbot/models/schemas.py
from datetime import datetime
from enum import Enum
from pydantic import BaseModel
from typing import Optional, List, Dict, Any

class MessageRole(str, Enum):
    user = "user"
    assistant = "assistant"
    system = "system"

class Intent(str, Enum):
    injury_report = "injury_report"
    soreness_report = "soreness_report"
    motivation_request = "motivation_request"
    plan_question = "plan_question"
    plan_adjustment_request = "plan_adjustment_request"
    fitness_question = "fitness_question"
    health_question = "health_question"
    progress_update = "progress_update"
    general_conversation = "general_conversation"

class ConversationMessage(BaseModel):
    role: MessageRole
    content: str
    timestamp: Optional[datetime] = None
    intent: Optional[Intent] = None

class MemoryChunk(BaseModel):
    content: str
    category: str
    importance: float = 0.5

class PlanChangeRequest(BaseModel):
    change_type: str
    reason: str
    affected_module: str
    suggested_modification: str
    urgency: str

class ChatRequest(BaseModel):
    user_id: str
    message: str
    session_id: str
    exercise_hint: str = ""

class ChatResponse(BaseModel):
    user_id: str
    session_id: str
    response: str
    intent_detected: Intent
    memories_used: List[str]
    plan_change_request: Optional[PlanChangeRequest] = None
    new_memories_stored: int

class ContextInjectRequest(BaseModel):
    user_id: str
    workout_plan: Optional[Dict[str, Any]] = None
    dietary_plan: Optional[Dict[str, Any]] = None
    form_feedback: Optional[Dict[str, Any]] = None

class HistoryResponse(BaseModel):
    user_id: str
    session_id: str
    messages: List[ConversationMessage]
    total_count: int
