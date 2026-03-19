from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# -------------------------------
# Models (Structured Input)
# -------------------------------

class UserProfile(BaseModel):
    name: Optional[str]
    age: int
    gender: str
    height: float
    weight: float

class FitnessGoal(BaseModel):
    primary_goal: str
    target_weight: Optional[float]
    timeline_weeks: Optional[int]

class HealthInfo(BaseModel):
    conditions: List[str]
    injuries: List[str]

class Lifestyle(BaseModel):
    activity_level: str
    available_time_per_day: int
    preferred_workout_time: str

class Diet(BaseModel):
    type: str
    restrictions: List[str]

class UserRequest(BaseModel):
    user_profile: UserProfile
    fitness_goal: FitnessGoal
    health_info: HealthInfo
    lifestyle: Lifestyle
    diet: Diet
    user_message: str


# -------------------------------
# ML / LLM Function
# -------------------------------

def ml_model_process(data: dict):
    
    # Prompt ban raha hai structured data se
    prompt = f"""
    User Details:
    Age: {data['user_profile']['age']}
    Weight: {data['user_profile']['weight']}
    Goal: {data['fitness_goal']['primary_goal']}
    Injuries: {data['health_info']['injuries']}
    Diet: {data['diet']['type']}

    User Message:
    {data['user_message']}

    Generate:
    1. Workout Plan
    2. Diet Suggestion
    3. Tips
    """

    # Dummy response (replace with GPT later)
    return {
        "workout_plan": "Cardio + Strength 5 days/week",
        "diet_plan": "High protein vegetarian diet",
        "tips": "Avoid sugar, stay hydrated"
    }


# -------------------------------
# API Endpoint
# -------------------------------

@app.post("/generate-plan")
async def generate_plan(request: UserRequest):
    
    # Step 1: JSON → dict
    data = request.dict()

    # Step 2: ML ko pass
    result = ml_model_process(data)

    # Step 3: Return JSON
    return {
        "success": True,
        "response": result
    }