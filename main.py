from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional, Dict, Any

# ✅ Your pipelines
from AI.workoutgenerator import workout_pipeline
from AI.mealplanner import meal_pipeline
from AI.form_analysis.routers.form import analyze_form_pipeline
from AI.form_analysis.pipeline.gemini_analyzer import analyze_with_gemini

# ✅ OpenAI config
from AI.form_analysis.config.settings import openai_client, MODEL

app = FastAPI()

# -------------------------------
# CORS
# -------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------
# Request Models
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


class ChatRequest(BaseModel):
    user: Dict[str, Any]
    message: str
    todayPlan: Optional[Dict[str, Any]] = None
    planName: Optional[str] = ""

    # 🔥 form analysis support
    frame_analyses: Optional[list] = None
    frames: Optional[list] = None
    exercise_hint: Optional[str] = ""
    perceived_difficulty: Optional[str] = ""


# -------------------------------
# Workout Plan API
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
# Video Analysis API
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

    return result


# -------------------------------
# Meal Plan API
# -------------------------------
@app.post("/meal-plan")
async def generate_meal_plan(request: UserRequest):
    print("🍽️ MEAL API CALLED")

    data = request.dict()
    result = meal_pipeline(data)

    return {
        "success": True,
        "user": data["name"],
        "meal_plan": result
    }


# -------------------------------
# Chat API (AI Coach)
# -------------------------------
@app.post("/chat")
async def chat_with_ai(request: ChatRequest):
    try:
        user = request.user
        message = request.message

        # =========================================================
        # 🔥 1. FORM ANALYSIS MODE
        # =========================================================
        if request.frames and request.frame_analyses:
            print("⚡ Running form analysis...")

            result = analyze_with_gemini(
                frames=request.frames,
                frame_analyses=request.frame_analyses,
                exercise_hint=request.exercise_hint,
                perceived_difficulty=request.perceived_difficulty
            )

            return {
                "success": True,
                "type": "analysis",
                "data": result
            }

        # =========================================================
        # 💬 2. CHAT MODE
        # =========================================================
        print("💬 Running chat...")

        prompt = f"""
You are a smart AI fitness coach.

User:
- Name: {user.get('name')}
- Goal: {user.get('fitnessGoals')}

User message:
"{message}"
"""

        # 👉 Inject workout context
        if request.todayPlan:
            prompt += f"""

Today's Plan ({request.planName}):
Focus: {request.todayPlan.get('focus')}

Exercises:
"""
            for ex in request.todayPlan.get("exercises", []):
                prompt += f"- {ex.get('name')} ({ex.get('sets')} x {ex.get('reps')})\n"

        prompt += """
Reply in Hinglish like a real coach.
Keep it short, motivating, and practical.
"""

        # 🔥 OpenAI call
        response = openai_client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}]
        )

        reply = response.choices[0].message.content.strip()

        reply = reply.strip()

        return {
            "success": True,
            "type": "chat",
            "reply": reply
        }

    except Exception as e:
        print("❌ CHAT ERROR:", str(e))
        return {
            "success": False,
            "error": str(e)
        }