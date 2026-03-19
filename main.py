from fastapi import FastAPI, UploadFile, File, Form
from pydantic import BaseModel
from typing import List, Optional
from fastapi.middleware.cors import CORSMiddleware
from AI.workoutgenerator import workout_pipeline

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
    try:
        await video.read()

        return {
            "success": True,
            "feedback": {
                "exercise_detected": exercise_hint or "pushup",
                "form_score": 7,
                "is_correct_form": False,
                "issues": [
                    {
                        "timestamp_seconds": 3,
                        "joint_or_body_part": "elbow",
                        "observation": "Elbow flare out ho raha hai",
                        "correction_cue": "Elbows ko body ke close rakho",
                        "severity": "moderate"
                    }
                ],
                "overall_summary": "Form thoda improve karna hai",
                "priority_correction": "Elbow alignment fix karo"
            }
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

# -------------------------------
# Meal Plan API (FIXED)
# -------------------------------
@app.post("/meal-plan")
async def generate_meal_plan(request: UserRequest):
    print("MEAL API CALLED")
    data = request.dict()

    # abhi demo ke liye simple response
    return {
        "success": True,
        "user": data["name"],
        "meal_plan": {
            "breakfast": "Oats + fruits",
            "lunch": "2 roti + sabzi",
            "dinner": "Light khichdi",
            "tips": "Avoid sugar, drink more water"
        }
    }