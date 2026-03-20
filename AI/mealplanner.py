import os
import json
import time
from typing import Dict
from dotenv import load_dotenv
from openai import OpenAI

# ==============================
# CONFIG
# ==============================

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
openai_client = OpenAI(api_key=OPENAI_API_KEY)
MODEL = "gpt-4o-mini"

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

AVAILABLE FOODS:
{json.dumps(foods, indent=2)}

Create a balanced full-day meal plan strictly choosing from the AVAILABLE FOODS.
RULES:
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

# ==============================
# MAIN PIPELINE
# ==============================

def meal_pipeline(user_input: Dict):
    preference = user_input.get("dietaryPreferences", ["veg"])[0]
    target_calories = calculate_calorie_target(user_input)

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