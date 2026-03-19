import google.genai as genai
import json

# ==============================
# CONFIG
# ==============================
load_dotenv()
API_KEY = os.getenv("GENAI_API_KEY")
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
# USER INPUT
# ==============================

user_input = {
    "name": "Ritika Tiwari",
    "age": 21,
    "weight": 65,
    "activityLevel": "sedentary",
    "fitnessGoals": ["weight-loss"],
    "dietaryPreferences": ["vegetarian"],
    "targetWeight": 50
}

# ==============================
# CALORIE TARGET LOGIC
# ==============================

def calculate_calorie_target(user):
    # simple weight loss logic
    base = user["weight"] * 22   # maintenance approx
    deficit = 500               # fat loss
    return int(base - deficit)

# ==============================
# MEMORY
# ==============================

memory = {
    "goal": "weight-loss meal plan",
    "preference": user_input["dietaryPreferences"][0],
    "target_calories": calculate_calorie_target(user_input),
    "current_calories": 0,
    "selected_meals": [],
    "attempted_meals": [],
    "plan_complete": False
}

# ==============================
# AI PLANNER
# ==============================

def ai_meal_planner(memory, foods):

    prompt = f"""
You are an AI diet planning agent.

GOAL: {memory['goal']}
TARGET CALORIES: {memory['target_calories']}
CURRENT CALORIES: {memory['current_calories']}

SELECTED: {memory['selected_meals']}
FAILED: {memory['attempted_meals']}

FOOD OPTIONS:
{foods}

TASK:
Select the NEXT BEST food item.

RULES:
- Must be vegetarian
- Must keep total calories within target
- Prefer low calorie if close to limit
- Do NOT repeat items
- Respond ONLY with food name
"""

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    return response.text.strip()

# ==============================
# MEAL AGENT
# ==============================

def meal_agent():

    while not memory["plan_complete"]:

        choice = ai_meal_planner(memory, FOODS)

        food = next((f for f in FOODS if f["name"] == choice), None)

        if not food:
            memory["attempted_meals"].append(choice)
            continue

        if food["name"] in [m["name"] for m in memory["selected_meals"]]:
            continue

        # calorie constraint
        if memory["current_calories"] + food["calories"] > memory["target_calories"]:
            memory["attempted_meals"].append(choice)
            continue

        # accept
        memory["selected_meals"].append({
            "name": food["name"],
            "calories": food["calories"]
        })

        memory["current_calories"] += food["calories"]

        # stop condition
        if memory["current_calories"] >= memory["target_calories"] * 0.9:
            memory["plan_complete"] = True

    # ==============================
    # FINAL JSON OUTPUT
    # ==============================

    output = {
        "user": user_input["name"],
        "target_calories": memory["target_calories"],
        "total_calories": memory["current_calories"],
        "meals": memory["selected_meals"]
    }

    print(json.dumps(output, indent=2))


# ==============================
# RUN
# ==============================

if __name__ == "__main__":
    meal_agent()