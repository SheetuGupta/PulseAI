from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from fastapi.middleware.cors import CORSMiddleware
from AI.workoutgenerator import workout_pipeline
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


# -------------------------------
# API Endpoint
# -------------------------------
@app.post("/generate-plan")
async def generate_plan(request: UserRequest):

    data = request.dict()

    result = workout_pipeline(data)
    return {
        "success": True,
        "user": data["name"],
        "response": result
    }