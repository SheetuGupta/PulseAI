# coaching_chatbot/agent/intent_detector.py
<<<<<<< HEAD
import google.generativeai as genai
from config.settings import MODEL
=======
from config.settings import openai_client, MODEL
>>>>>>> 12c61aafb90e4a90001d8632bfb95c95278aab20
from models.schemas import Intent

INTENT_PROMPT_TEMPLATE = """
Classify the intent of this fitness coaching message into exactly one of these categories:

injury_report — user mentions a new or existing injury, pain, or physical limitation
soreness_report — user mentions muscle soreness, fatigue, or tiredness that is not an injury
motivation_request — user is feeling unmotivated, wants encouragement, or is struggling mentally
plan_question — user asks about their current workout or diet plan without requesting changes
plan_adjustment_request — user wants to change or modify their workout or diet plan
fitness_question — user asks a general fitness question not specific to their plan
health_question — user asks a general health or wellness question that is not clinical
progress_update — user shares a progress update or achievement
general_conversation — everything else

Message to classify: {message}

Respond with only the category name.
No explanation. No punctuation. Just the category.
"""


def detect_intent(message: str) -> Intent:
    prompt = INTENT_PROMPT_TEMPLATE.format(message=message)
<<<<<<< HEAD
    model = genai.GenerativeModel(MODEL)
    response = model.generate_content(prompt)
    raw = response.text.strip().lower()
=======
    response = openai_client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        max_tokens=20,
    )
    raw = response.choices[0].message.content.strip().lower()
>>>>>>> 12c61aafb90e4a90001d8632bfb95c95278aab20
    raw = raw.replace(" ", "_").strip(".")
    try:
        return Intent(raw)
    except ValueError:
        return Intent.general_conversation
