import os
import json
import time
from typing import Dict, List
from dotenv import load_dotenv
<<<<<<< HEAD
import google.generativeai as genai
=======
from openai import OpenAI
>>>>>>> 12c61aafb90e4a90001d8632bfb95c95278aab20

# ==============================
# CONFIG
# ==============================

<<<<<<< HEAD
load_dotenv(override=True)
API_KEY = os.getenv("GEMINI_API_KEY") or "UNSET_API_KEY"
genai.configure(api_key=API_KEY)

MODEL = "gemini-1.5-flash"
model = genai.GenerativeModel(MODEL)
=======
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
openai_client = OpenAI(api_key=OPENAI_API_KEY)
MODEL = "gpt-4o-mini"
>>>>>>> 12c61aafb90e4a90001d8632bfb95c95278aab20

# ==============================
# SAFE LLM CALL
# ==============================

<<<<<<< HEAD
def call_llm(prompt: str) -> str:
    response = model.generate_content(prompt)
    return response.text.strip()
=======
def call_llm(prompt: str, retries: int = 3) -> str:
    """Call OpenAI with exponential backoff on rate limit errors."""
    for attempt in range(retries):
        try:
            response = openai_client.chat.completions.create(
                model=MODEL,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            err = str(e)
            is_rate_limit = "429" in err or "rate_limit" in err.lower()
            if is_rate_limit and attempt < retries - 1:
                wait = 2 ** attempt
                print(f"[RATE LIMIT] Retrying in {wait}s... (attempt {attempt + 1}/{retries})")
                time.sleep(wait)
                continue
            print(f"[LLM ERROR] {e}")
            raise RuntimeError(f"OpenAI call failed: {e}")
>>>>>>> 12c61aafb90e4a90001d8632bfb95c95278aab20

# ==============================
# SAFE JSON PARSER
# ==============================

def safe_json_parse(text: str):
    if text.startswith("```json"):
        text = text[7:]
    elif text.startswith("```"):
        text = text[3:]
    if text.endswith("```"):
        text = text[:-3]
    text = text.strip()
    try:
        return json.loads(text)
    except Exception:
        start = text.find("{")
        end = text.rfind("}") + 1
        if start != -1 and end > start:
            return json.loads(text[start:end])
        raise ValueError("Could not parse JSON from LLM response")

# ==============================
# EXERCISE DATABASE (RAG)
# ==============================

EXERCISE_DB = [
  {"name": "Push-ups", "type": "strength", "level": "beginner"},
  {"name": "Incline Push-ups", "type": "strength", "level": "beginner"},
  {"name": "Knee Push-ups", "type": "strength", "level": "beginner"},
  {"name": "Decline Push-ups", "type": "strength", "level": "intermediate"},
  {"name": "Diamond Push-ups", "type": "strength", "level": "intermediate"},
  {"name": "Archer Push-ups", "type": "strength", "level": "advanced"},
  {"name": "Pseudo Planche Push-ups", "type": "strength", "level": "advanced"},
  {"name": "One-arm Push-ups", "type": "strength", "level": "advanced"},

  {"name": "Squats", "type": "strength", "level": "beginner"},
  {"name": "Wall Sit", "type": "strength", "level": "beginner"},
  {"name": "Glute Bridge", "type": "strength", "level": "beginner"},
  {"name": "Lunges", "type": "strength", "level": "beginner"},
  {"name": "Bulgarian Split Squats", "type": "strength", "level": "intermediate"},
  {"name": "Jump Squats", "type": "strength", "level": "intermediate"},
  {"name": "Pistol Squats", "type": "strength", "level": "advanced"},
  {"name": "Shrimp Squats", "type": "strength", "level": "advanced"},

  {"name": "Plank", "type": "core", "level": "beginner"},
  {"name": "Side Plank", "type": "core", "level": "beginner"},
  {"name": "Dead Bug", "type": "core", "level": "beginner"},
  {"name": "Crunches", "type": "core", "level": "beginner"},
  {"name": "Leg Raises", "type": "core", "level": "beginner"},
  {"name": "Russian Twists", "type": "core", "level": "intermediate"},
  {"name": "Hanging Leg Raises", "type": "core", "level": "advanced"},
  {"name": "Dragon Flag", "type": "core", "level": "advanced"},
  {"name": "V-ups", "type": "core", "level": "intermediate"},
  {"name": "Flutter Kicks", "type": "core", "level": "beginner"},

  {"name": "Jumping Jacks", "type": "cardio", "level": "beginner"},
  {"name": "High Knees", "type": "cardio", "level": "beginner"},
  {"name": "Butt Kicks", "type": "cardio", "level": "beginner"},
  {"name": "Burpees", "type": "cardio", "level": "intermediate"},
  {"name": "Mountain Climbers", "type": "cardio", "level": "intermediate"},
  {"name": "Skaters", "type": "cardio", "level": "intermediate"},
  {"name": "Tuck Jumps", "type": "cardio", "level": "advanced"},
  {"name": "Sprint Intervals", "type": "cardio", "level": "advanced"},

  {"name": "Superman Hold", "type": "strength", "level": "beginner"},
  {"name": "Reverse Snow Angels", "type": "strength", "level": "beginner"},
  {"name": "Back Extensions", "type": "strength", "level": "intermediate"},
  {"name": "Pull-ups", "type": "strength", "level": "intermediate"},
  {"name": "Chin-ups", "type": "strength", "level": "intermediate"},
  {"name": "Australian Pull-ups", "type": "strength", "level": "beginner"},
  {"name": "Muscle-ups", "type": "strength", "level": "advanced"},

  {"name": "Dips", "type": "strength", "level": "intermediate"},
  {"name": "Bench Dips", "type": "strength", "level": "beginner"},
  {"name": "Tricep Extensions (Bodyweight)", "type": "strength", "level": "intermediate"},

  {"name": "Calf Raises", "type": "strength", "level": "beginner"},
  {"name": "Single-leg Calf Raises", "type": "strength", "level": "intermediate"},

  {"name": "Plank Shoulder Taps", "type": "core", "level": "intermediate"},
  {"name": "Hollow Body Hold", "type": "core", "level": "intermediate"},
  {"name": "L-sit", "type": "core", "level": "advanced"},

  {"name": "Bear Crawl", "type": "cardio", "level": "intermediate"},
  {"name": "Crab Walk", "type": "cardio", "level": "beginner"},
  {"name": "Broad Jumps", "type": "cardio", "level": "intermediate"},

  {"name": "Handstand Hold", "type": "strength", "level": "advanced"},
  {"name": "Handstand Push-ups", "type": "strength", "level": "advanced"},

  {"name": "Neck Flexion", "type": "strength", "level": "beginner"},
  {"name": "Neck Extension", "type": "strength", "level": "beginner"},

  {"name": "Jump Rope", "type": "cardio", "level": "beginner"},
  {"name": "Shadow Boxing", "type": "cardio", "level": "intermediate"},
]

# ==============================
# STEP 1: NORMALIZE INPUT
# ==============================

def normalize_input(user_json: Dict) -> Dict:
    return {
        "name": user_json.get("name"),
        "age": user_json.get("age"),
        "weight": user_json.get("weight"),
        "fitness_level": user_json.get("activityLevel", "beginner"),
        "goal": user_json.get("fitnessGoals", ["general"])[0],
        "diet": user_json.get("dietaryPreferences", []),
        "health_conditions": user_json.get("healthConditions", []),
        "target_weight": user_json.get("targetWeight"),
    }

# ==============================
# AGENT 1: ANALYZER
# ==============================

def analyze_user(user: Dict) -> Dict:
    prompt = f"""You are a fitness analyst AI.

Analyze this user and return structured insights.

USER:
{json.dumps(user)}

STRICT:
- Output ONLY JSON (no markdown, no backticks, no explanation)

FORMAT:
{{
  "fitness_category": "",
  "intensity": "",
  "focus": [],
  "risk_notes": []
}}
"""
    text = call_llm(prompt)
    return safe_json_parse(text)

# ==============================
# AGENT 2: RAG RETRIEVER
# ==============================

def retrieve_exercises(analysis: Dict) -> List[Dict]:
    level = analysis.get("fitness_category", "beginner")
    return [
        ex for ex in EXERCISE_DB
        if ex["level"] == level or ex["level"] == "beginner"
    ]

# ==============================
# AGENT 3: WORKOUT PLANNER
# ==============================

def generate_plan(user: Dict, analysis: Dict, exercises: List[Dict]):
    prompt = f"""You are an expert fitness coach AI.

USER:
{json.dumps(user)}

ANALYSIS:
{json.dumps(analysis)}

AVAILABLE EXERCISES:
{json.dumps(exercises)}

Create a personalized 7-day workout plan.

STRICT:
- Output ONLY JSON (no markdown, no backticks, no explanation)

FORMAT:
{{
  "plan_name": "",
  "weekly_schedule": [
    {{
      "day": "",
      "focus": "",
      "exercises": [
        {{
          "name": "",
          "sets": "",
          "reps": "",
          "rest": ""
        }}
      ]
    }}
  ]
}}
"""
    text = call_llm(prompt)
    return safe_json_parse(text)

# ==============================
# MAIN PIPELINE
# ==============================

def workout_pipeline(raw_input: Dict):
    user = normalize_input(raw_input)
    analysis = analyze_user(user)
    exercises = retrieve_exercises(analysis)
    plan = generate_plan(user, analysis, exercises)

    return {
        "user": user["name"],
        "analysis": analysis,
        "workout_plan": plan,
    }