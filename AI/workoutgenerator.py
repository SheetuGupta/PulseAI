import os
import json
from typing import Dict, List
from dotenv import load_dotenv
from google import genai

# ==============================
# CONFIG
# ==============================

load_dotenv(override=True)
API_KEY = os.getenv("GENAI_API_KEY") or os.getenv("GEMINI_API_KEY") or "UNSET_API_KEY"
client = genai.Client(api_key=API_KEY)

MODEL = "gemini-2.5-flash-lite"

# ==============================
# SAFE LLM CALL
# ==============================

def call_llm(prompt: str) -> str:
    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )
    return response.text.strip()

# ==============================
# SAFE JSON PARSER
# ==============================

def safe_json_parse(text: str):
    try:
        return json.loads(text)
    except:
        start = text.find("{")
        end = text.rfind("}") + 1
        return json.loads(text[start:end])

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
  {"name": "Shadow Boxing", "type": "cardio", "level": "intermediate"}
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
        "target_weight": user_json.get("targetWeight")
    }

# ==============================
# AGENT 1: ANALYZER
# ==============================

def analyze_user(user: Dict) -> Dict:

    prompt = f"""
You are a fitness analyst AI.

Analyze this user and return structured insights.

USER:
{json.dumps(user)}

STRICT:
- Output ONLY JSON

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

    prompt = f"""
You are an expert fitness coach AI.

USER:
{json.dumps(user)}

ANALYSIS:
{json.dumps(analysis)}

AVAILABLE EXERCISES:
{json.dumps(exercises)}

Create a personalized workout plan.

STRICT:
- Output ONLY JSON
- No explanation

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
        "workout_plan": plan
    }

# ==============================
# TEST INPUT
# ==============================

if __name__ == "__main__":

    result = workout_pipeline(input_json)

    print(json.dumps(result, indent=2))