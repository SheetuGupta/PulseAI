import os
import json
import time
from typing import Dict
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
print("API KEY:", API_KEY)
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
# FOOD DATABASE
# ==============================

FOODS = [
    {"name": "Oats", "type": "veg", "category": "breakfast", "calories": 150},
    {"name": "Poha", "type": "veg", "category": "breakfast", "calories": 180},
    {"name": "Upma", "type": "veg", "category": "breakfast", "calories": 200},
    {"name": "Idli + Sambar", "type": "veg", "category": "breakfast", "calories": 220},
    {"name": "Boiled Eggs", "type": "non-veg", "category": "breakfast", "calories": 140},
    {"name": "Roti + Sabzi", "type": "veg", "category": "lunch", "calories": 300},
    {"name": "Dal + Rice", "type": "veg", "category": "lunch", "calories": 350},
    {"name": "Chicken Rice Bowl", "type": "non-veg", "category": "lunch", "calories": 420},
    {"name": "Paneer Curry", "type": "veg", "category": "dinner", "calories": 400},
    {"name": "Grilled Chicken", "type": "non-veg", "category": "dinner", "calories": 350},
    {"name": "Salad", "type": "veg", "category": "any", "calories": 100},
    {"name": "Fruits", "type": "veg", "category": "snack", "calories": 120},
    {"name": "Greek Yogurt", "type": "veg", "category": "snack", "calories": 100},
    {"name": "Protein Bar", "type": "veg", "category": "snack", "calories": 180},
    {"name": "Mixed Nuts", "type": "veg", "category": "snack", "calories": 160},
    {"name": "Sprouts", "type": "veg", "category": "snack", "calories": 90},
]

# ==============================
# CALORIE TARGET
# ==============================

def calculate_calorie_target(user: Dict) -> int:
    base = user["weight"] * 22
    deficit = 500
    return int(base - deficit)

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
        start = text.find("[")
        end = text.rfind("]") + 1
        if start != -1 and end > start:
            try:
                return json.loads(text[start:end])
            except Exception:
                pass
        return []

# ==============================
# AI CALL
# ==============================

def generate_full_meal_plan(target_calories: int, preference: str, foods: list) -> list:
    prompt = f"""You are an expert AI Dietitian.
TARGET CALORIES: {target_calories}
DIET PREFERENCE: {preference}

<<<<<<< HEAD
    prompt = f"""
You are an AI diet planning agent.

TARGET CALORIES: {memory['target_calories']}

FOOD OPTIONS:
=======
AVAILABLE FOODS:
>>>>>>> 12c61aafb90e4a90001d8632bfb95c95278aab20
{json.dumps(foods, indent=2)}

Create a balanced full-day meal plan strictly choosing from the AVAILABLE FOODS.
RULES:
<<<<<<< HEAD
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
=======
1. Try to hit target calories within a +/- 10% margin.
2. Ensure variety (include breakfast, lunch, dinner, snack).
3. Provide ONLY a JSON array of selected food objects. No markdown, no backticks, just raw JSON.
4. Each object must have ONLY the keys "name" and "calories".

Example format:
[
  {{"name": "Oats", "calories": 150}},
  {{"name": "Roti + Sabzi", "calories": 300}}
]
"""
    for attempt in range(3):
        try:
            response = openai_client.chat.completions.create(
                model=MODEL,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
            )
            text = response.choices[0].message.content.strip()
            return safe_json_parse(text)
        except Exception as e:
            err = str(e)
            if ("429" in err or "rate_limit" in err.lower()) and attempt < 2:
                wait = 2 ** attempt
                print(f"[RATE LIMIT] Meal plan retry in {wait}s...")
                time.sleep(wait)
                continue
            print(f"[MEAL LLM ERROR] {e}")
            return []
    return []
>>>>>>> 12c61aafb90e4a90001d8632bfb95c95278aab20

# ==============================
# MAIN PIPELINE
# ==============================

def meal_pipeline(user_input: Dict):
    preference = user_input.get("dietaryPreferences", ["veg"])[0]
    target_calories = calculate_calorie_target(user_input)

<<<<<<< HEAD
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
=======
    selected_meals = generate_full_meal_plan(target_calories, preference, FOODS)
    total_calories = sum(m.get("calories", 0) for m in selected_meals)

    if not selected_meals:
        return {
            "user": user_input["name"],
            "error": "Meal generation failed. Please try again.",
        }

    return {
        "user": user_input["name"],
        "target_calories": target_calories,
        "total_calories": total_calories,
        "meals": selected_meals,
    }
>>>>>>> 12c61aafb90e4a90001d8632bfb95c95278aab20
