from fastapi import FastAPI, UploadFile, File, Form
from pydantic import BaseModel
from typing import List, Optional
from fastapi.middleware.cors import CORSMiddleware
from AI.workoutgenerator import workout_pipeline
from AI.mealplanner import meal_pipeline
from AI.form_analysis.routers.form import analyze_form_pipeline
from fastapi import UploadFile, File, Form

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------
# Request Model
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
# Generate Workout Plan API
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

# -------------------------------
# Analyze Video API (Mock Version)
# -------------------------------
@app.post("/analyze-video")
async def analyze_video(
    video: UploadFile = File(...),
    exercise_hint: str = Form(""),
    perceived_difficulty: str = Form("")
):
    print("🔥 VIDEO ANALYSIS API HIT")

    video_bytes = await video.read()

    result = analyze_form_pipeline(
        video_bytes,
        exercise_hint,
        perceived_difficulty
    )

    print("✅ ANALYSIS RESULT:", result)

    return result
# -------------------------------
# Meal Plan API (FIXED)
# -------------------------------
@app.post("/meal-plan")
async def generate_meal_plan(request: UserRequest):
    print("MEAL API CALLED")

    data = request.dict()   # ✅ define data

    result = meal_pipeline(data)   # ✅ correct function

    return {
        "success": True,
        "user": data["name"],
        "meal_plan": result
    }
