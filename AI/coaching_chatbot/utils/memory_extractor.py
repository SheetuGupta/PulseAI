# coaching_chatbot/utils/memory_extractor.py
from config.settings import openai_client, MODEL
from models.schemas import MemoryChunk
from datetime import datetime
import json

EXTRACTION_PROMPT = """
You are a memory extraction system for a fitness
coaching AI. After each conversation turn, you
extract important facts about the user worth
remembering for future sessions.

Read this conversation turn:
USER: {user_message}
COACH: {assistant_message}
DETECTED INTENT: {intent}

Extract 0 to 4 important facts about the user.
Only extract facts that are:
- New information not likely already known
- Relevant to future fitness coaching sessions
- Specific and factual, not vague

Categories:
- injury: any injury, pain, or physical limitation
- soreness: soreness or fatigue patterns
- motivation: motivational patterns, what helps them
- preference: exercise preferences, dislikes, schedule
- progress: PRs, weight changes, achievements
- goal: goal updates or changes
- general: other relevant personal facts

Importance scores:
- injury facts: 0.9
- medical or serious facts: 0.9
- goal changes: 0.8
- preferences: 0.5
- progress: 0.6
- general: 0.3

Return ONLY valid JSON array. No markdown. No text.
Empty array if nothing worth extracting.

[
  {
    "content": "factual statement about the user",
    "category": "category name",
    "importance": 0.0 to 1.0
  }
]

Examples of good memory facts:
"User reported left knee pain on {today},
 rated 6 out of 10 severity"
"User dislikes burpees and jumping exercises"
"User feels most motivated when working out with music"
"User hit a new squat PR of 80kg"
"User struggles with consistency on weekends"
"User is training for a 5K race in March"
"User has been feeling demotivated for the past week"

Examples of bad memory facts (do not extract these):
"User said hello" — too trivial
"User asked about their plan" — not a personal fact
"User wants to work out" — too vague
"""

def extract_memories(user_message: str, assistant_message: str, intent: str) -> list[MemoryChunk]:
    if intent in ["general_conversation", "plan_question", "fitness_question"]:
        return []
        
    prompt = EXTRACTION_PROMPT.format(
        user_message=user_message,
        assistant_message=assistant_message,
        intent=intent,
        today=datetime.now().strftime("%Y-%m-%d")
    )
    
    try:
        response = openai_client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}]
        )
        text = response.choices[0].message.content.strip()
        text = text.replace("```json", "").replace("```", "").strip()
        parsed = json.loads(text)
        return [MemoryChunk(**item) for item in parsed]
    except Exception:
        return []
