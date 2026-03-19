import os
import json
from typing import Dict
from dotenv import load_dotenv
from google import genai
# ==============================
# CONFIG
# ==============================

load_dotenv()
API_KEY = os.getenv("GENAI_API_KEY")
print("API KEY:", API_KEY)
client = genai.Client(api_key=API_KEY)
MODEL = "gemini-2.5-flash"

# ==============================
# FOOD DATABASE
# ==============================

FOODS = [
    {"name": "Oats", "type": "veg", "category": "breakfast", "calories": 150},
    {"name": "Poha", "type": "veg", "category": "breakfast", "calories": 180},
    {"name": "Upma", "type": "veg", "category": "breakfast", "calories": 200},
    {"name": "Roti + Sabzi", "type": "veg", "category": "lunch", "calories": 300},
    {"name": "Dal + Rice", "type": "veg", "category": "lunch", "calories": 350},
    {"name": "Paneer Curry", "type": "veg", "category": "dinner", "calories": 400},
    {"name": "Salad", "type": "veg", "category": "any", "calories": 100},
    {"name": "Fruits", "type": "veg", "category": "snack", "calories": 120},
]

# ==============================
# CALORIE TARGET
# ==============================

def calculate_calorie_target(user: Dict):
    base = user["weight"] * 22
    deficit = 500
    return int(base - deficit)

# ==============================
# AI CALL
# ==============================

def ai_meal_planner(memory, foods):

    prompt = f"""
You are an AI diet planning agent.

TARGET CALORIES: {memory['target_calories']}
CURRENT CALORIES: {memory['current_calories']}

SELECTED: {memory['selected_meals']}
FAILED: {memory['attempted_meals']}

FOOD OPTIONS:
{foods}

RULES:
- Must be vegetarian
- Must not exceed calories
- Do NOT repeat
- Respond ONLY with food name
"""

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    return response.text.strip()

# ==============================
# MAIN PIPELINE (IMPORTANT)
# ==============================

def meal_pipeline(user_input: Dict):

    memory = {
        "goal": "weight-loss meal plan",
        "preference": user_input["dietaryPreferences"][0],
        "target_calories": calculate_calorie_target(user_input),
        "current_calories": 0,
        "selected_meals": [],
        "attempted_meals": [],
        "plan_complete": False
    }

    max_iterations = 20
    iterations = 0

    while not memory["plan_complete"] and iterations < max_iterations:
        iterations += 1

        choice = ai_meal_planner(memory, FOODS)
        print("AI RAW:", choice)

        food = next((f for f in FOODS if f["name"] == choice), None)

        if not food:
            memory["attempted_meals"].append(choice)
            continue

        if food["name"] in [m["name"] for m in memory["selected_meals"]]:
            continue

        if memory["current_calories"] + food["calories"] > memory["target_calories"]:
            memory["attempted_meals"].append(choice)
            continue

        memory["selected_meals"].append({
            "name": food["name"],
            "calories": food["calories"]
        })

        memory["current_calories"] += food["calories"]

        if memory["current_calories"] >= memory["target_calories"] * 0.9:
            memory["plan_complete"] = True

    if not memory["selected_meals"]:
        return {
            "user": user_input["name"],
            "error": "Meal generation failed"
        }

    return {
        "user": user_input["name"],
        "target_calories": memory["target_calories"],
        "total_calories": memory["current_calories"],
        "meals": memory["selected_meals"]
    }
# ==============================
# TEST
# ==============================

if __name__ == "__main__":

    result = meal_pipeline(input_json)

    print(json.dumps(result, indent=2))