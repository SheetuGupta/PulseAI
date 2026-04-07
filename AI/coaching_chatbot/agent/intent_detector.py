# coaching_chatbot/agent/intent_detector.py
import google.generativeai as genai
from config.settings import MODEL
from models.schemas import Intent

INTENT_PROMPT_TEMPLATE = """
Classify the intent of this fitness coaching
message into exactly one of these categories:

injury_report — user mentions a new or existing
  injury, pain, or physical limitation
  Examples: "my knee hurts", "I pulled my hamstring",
  "I have a sore shoulder"

soreness_report — user mentions muscle soreness,
  fatigue, or tiredness that is not an injury
  Examples: "my legs are sore", "I am exhausted",
  "I feel tired today"

motivation_request — user is feeling unmotivated,
  wants encouragement, or is struggling mentally
  Examples: "I don't feel like working out",
  "I am losing motivation", "help me stay on track"

plan_question — user asks about their current
  workout or diet plan without requesting changes
  Examples: "what is my plan for today",
  "what should I eat before training"

plan_adjustment_request — user wants to change
  or modify their workout or diet plan
  Examples: "can we change tomorrow's workout",
  "I want to train legs instead", "skip chest day"

fitness_question — user asks a general fitness
  question not specific to their plan
  Examples: "how many sets should I do for hypertrophy",
  "what is progressive overload"

health_question — user asks a general health or
  wellness question that is not clinical
  Examples: "how much sleep do I need",
  "should I train fasted"

progress_update — user shares a progress update
  or achievement
  Examples: "I hit a new PR today", "I lost 2kg",
  "I completed all my workouts this week"

general_conversation — everything else

Message to classify: {message}

Respond with only the category name.
No explanation. No punctuation. Just the category.
"""

def detect_intent(message: str) -> Intent:
    prompt = INTENT_PROMPT_TEMPLATE.format(message=message)
    model = genai.GenerativeModel(MODEL)
    response = model.generate_content(prompt)
    raw = response.text.strip().lower()
    raw = raw.replace(" ", "_").strip(".")
    try:
        return Intent(raw)
    except ValueError:
        return Intent.general_conversation
