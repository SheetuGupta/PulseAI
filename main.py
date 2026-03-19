from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for dev (Next.js runs on different port)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------
# Request Model (Frontend Match)
# -------------------------------
class UserRequest(BaseModel):
    name: str
    age: int
    weight: float
    activityLevel: str
    fitnessGoals: List[str]
    healthConditions: List[str]
    dietaryPreferences: List[str]
    healthIssues: Optional[str] = "none"
    targetWeight: Optional[float] = None


# -------------------------------
# ML Function
# -------------------------------
def ml_model_process(data: dict):

    # Array → single value convert
    goal = data["fitnessGoals"][0] if data["fitnessGoals"] else ""
    diet = data["dietaryPreferences"][0] if data["dietaryPreferences"] else ""
    condition = data["healthConditions"][0] if data["healthConditions"] else ""

    prompt = f"""
    Name: {data['name']}
    Age: {data['age']}
    Weight: {data['weight']}
    Activity Level: {data['activityLevel']}
    Goal: {goal}
    Target Weight: {data.get('targetWeight')}
    Health Condition: {condition}
    Diet: {diet}
    Issues: {data['healthIssues']}

    Generate:
    1. Workout Plan
    2. Diet Plan
    3. Tips
    """

    return {
        "workout_plan": f"Plan for {goal}: 30 min cardio + strength training",
        "diet_plan": f"{diet} based balanced diet",
        "tips": "Stay consistent and hydrated"
    }


# -------------------------------
# API Endpoint
# -------------------------------
@app.post("/generate-plan")
async def generate_plan(request: UserRequest):

    data = request.dict()

    result = ml_model_process(data)

    return {
        "success": True,
        "user": data["name"],
        "response": result
    }