import os
import json
from typing import Dict
from dotenv import load_dotenv
import google.generativeai as genai
# ==============================
# CONFIG
# ==============================

load_dotenv(override=True)
API_KEY = os.getenv("GEMINI_API_KEY") or "UNSET_API_KEY"
print("API KEY:", API_KEY)
genai.configure(api_key=API_KEY)
MODEL = "gemini-1.5-flash"
model = genai.GenerativeModel(MODEL)

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

FOOD OPTIONS:
{json.dumps(foods, indent=2)}

RULES:
- Must be vegetarian
- Total calories must be close to TARGET CALORIES (at least 90%)
- Do NOT repeat foods
- Respond ONLY with a valid JSON array of food names. For example: ["Oats", "Salad", "Paneer Curry"]
"""

    response = model.generate_content(prompt)
    text = response.text.strip()
    if text.startswith("```json"):
        text = text[7:]
    elif text.startswith("```"):
        text = text[3:]
    if text.endswith("```"):
        text = text[:-3]
    text = text.strip()
    
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return []

# ==============================
# MAIN PIPELINE (IMPORTANT)
# ==============================

def meal_pipeline(user_input: Dict):

    target_calories = calculate_calorie_target(user_input)

    memory = {
        "goal": "weight-loss meal plan",
        "preference": user_input.get("dietaryPreferences", ["veg"])[0] if user_input.get("dietaryPreferences") else "veg",
        "target_calories": target_calories,
    }

    choices = ai_meal_planner(memory, FOODS)
    print("AI RAW:", choices)

    selected_meals = []
    current_calories = 0

    if not isinstance(choices, list):
        choices = []

    for choice in choices:
        food = next((f for f in FOODS if f["name"] == choice), None)

        if not food:
            continue

        if food["name"] in [m["name"] for m in selected_meals]:
            continue

        if current_calories + food["calories"] > target_calories:
            continue

        selected_meals.append({
            "name": food["name"],
            "calories": food["calories"]
        })

        current_calories += food["calories"]

    if not selected_meals:
        return {
            "user": user_input.get("name", "Unknown"),
            "error": "Meal generation failed"
        }

    return {
        "user": user_input.get("name", "Unknown"),
        "target_calories": target_calories,
        "total_calories": current_calories,
        "meals": selected_meals
    }
# ==============================
# TEST
# ==============================

if __name__ == "__main__":

    input_json = {
        "name": "Vishal",
        "weight": 80,
        "dietaryPreferences": ["veg"]
    }

    result = meal_pipeline(input_json)

    print(json.dumps(result, indent=2))