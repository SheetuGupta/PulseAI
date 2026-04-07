import os
import json
from dotenv import load_dotenv
from fastapi import FastAPI, UploadFile, File, Form, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from openai import OpenAI
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from database import get_db
from models import User, Plan, ProgressLog

# ✅ AI pipelines
from AI.workoutgenerator import workout_pipeline
from AI.mealplanner import meal_pipeline
from AI.form_analysis.routers.form import analyze_form_pipeline
from AI.form_analysis.pipeline.openai_analyzer import analyze_with_openai

<<<<<<< HEAD
# ✅ Gemini config
import google.generativeai as genai
from AI.form_analysis.config.settings import MODEL
=======
# ==============================
# CONFIG
# ==============================
>>>>>>> 12c61aafb90e4a90001d8632bfb95c95278aab20

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
openai_client = OpenAI(api_key=OPENAI_API_KEY)
MODEL = "gpt-4o-mini"

app = FastAPI(title="PulseAI API", version="2.0")

# ==============================
# CORS
# ==============================
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:3001",
        "http://127.0.0.1:3001",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==============================
# REQUEST MODELS
# ==============================

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
    frame_analyses: Optional[list] = None
    frames: Optional[list] = None
    exercise_hint: Optional[str] = ""
    perceived_difficulty: Optional[str] = ""


class FeedbackRequest(BaseModel):
    user_id: str
    feedback: str
    perceived_difficulty: str
    weight_log: Optional[float] = None


# ==============================
# WORKOUT PLAN API
# ==============================

@app.post("/generate-plan")
async def generate_plan(request: UserRequest, db: AsyncSession = Depends(get_db)):
    data = request.dict()

    result = await db.execute(select(User).where(User.name == data["name"]))
    user = result.scalars().first()

    if not user:
        user = User(
            name=data["name"],
            age=data["age"],
            weight=data["weight"],
            activity_level=data["activityLevel"],
            fitness_goals=data.get("fitnessGoals", []),
            health_conditions=data.get("healthConditions", []),
            dietary_preferences=data.get("dietaryPreferences", []),
            target_weight=data.get("targetWeight"),
        )
        db.add(user)
        await db.flush()

    workout_result = workout_pipeline(data)

    new_plan = Plan(
        user_id=user.id,
        plan_type="workout",
        plan_data=workout_result,
    )
    db.add(new_plan)
    await db.commit()

    return {
        "success": True,
        "user_id": user.id,
        "user": data["name"],
        "response": workout_result,
    }


# ==============================
# VIDEO / FORM ANALYSIS API
# ==============================

@app.post("/analyze-video")
async def analyze_video(
    video: UploadFile = File(...),
    exercise_hint: str = Form(""),
    perceived_difficulty: str = Form(""),
):
    print("🔥 VIDEO ANALYSIS API HIT")
    video_bytes = await video.read()
    result = analyze_form_pipeline(video_bytes, exercise_hint, perceived_difficulty)
    return result


# ==============================
# MEAL PLAN API
# ==============================

@app.post("/meal-plan")
async def generate_meal_plan(request: UserRequest, db: AsyncSession = Depends(get_db)):
    print("🍽️ MEAL API CALLED")
    data = request.dict()
    result = meal_pipeline(data)

    db_res = await db.execute(select(User).where(User.name == data["name"]))
    user = db_res.scalars().first()
    if user:
        new_plan = Plan(user_id=user.id, plan_type="meal", plan_data=result)
        db.add(new_plan)
        await db.commit()

    return {
        "success": True,
        "user": data["name"],
        "meal_plan": result,
    }


# ==============================
# PROGRESS API
# ==============================

@app.get("/progress/{user_name}")
async def get_progress(user_name: str, db: AsyncSession = Depends(get_db)):
    res = await db.execute(select(User).where(User.name == user_name))
    user = res.scalars().first()
    if not user:
        return {"success": False, "error": "User not found"}

    logs_res = await db.execute(
        select(ProgressLog)
        .where(ProgressLog.user_id == user.id)
        .order_by(ProgressLog.date.asc())
    )
    logs = logs_res.scalars().all()

    weight_data = []
    for log in logs:
        if log.weight_log:
            weight_data.append({
                "date": log.date.strftime("%Y-%m-%d"),
                "weight": log.weight_log,
            })

    return {
        "success": True,
        "weight_data": weight_data,
        "total_logs": len(logs),
    }


# ==============================
# SUBMIT FEEDBACK API
# ==============================

@app.post("/submit-feedback")
async def submit_feedback(req: FeedbackRequest, db: AsyncSession = Depends(get_db)):
    log = ProgressLog(
        user_id=req.user_id,
        plan_type="workout",
        feedback=req.feedback,
        perceived_difficulty=req.perceived_difficulty,
        weight_log=req.weight_log,
    )
    db.add(log)

    if req.weight_log:
        result = await db.execute(select(User).where(User.id == req.user_id))
        user = result.scalars().first()
        if user:
            user.weight = req.weight_log

    prompt = (
        f"You are a motivational fitness coach. "
        f"User feedback: '{req.feedback}'. Perceived difficulty: '{req.perceived_difficulty}'. "
        f"Write ONE short, encouraging sentence with a practical adjustment for their next session."
    )
    response = openai_client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8,
    )
    ai_reply = response.choices[0].message.content.strip()

    await db.commit()
    return {"success": True, "ai_adjustment_note": ai_reply}


# ==============================
# CHAT API (AI Coach)
# ==============================

@app.post("/chat")
async def chat_with_ai(request: ChatRequest):
    try:
        user = request.user
        message = request.message

        if request.frames and request.frame_analyses:
            print("⚡ Running form analysis...")
            result = analyze_with_openai(
                frames=request.frames,
                frame_analyses=request.frame_analyses,
                exercise_hint=request.exercise_hint,
                perceived_difficulty=request.perceived_difficulty,
            )
            return {"success": True, "type": "analysis", "data": result}

        print("💬 Running chat...")
<<<<<<< HEAD

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

        # 🔥 Gemini call
        model = genai.GenerativeModel(MODEL)
        response = model.generate_content(prompt)

        reply = response.text.strip()
=======
        system_msg = (
            "You are a smart AI fitness coach. Speak in Hinglish (mix of Hindi and English), "
            "like a real personal trainer — motivating, direct, and practical. Keep it concise."
        )
        user_msg = f"User Name: {user.get('name')}\nFitness Goal: {user.get('fitnessGoals')}\n"

        if request.todayPlan:
            user_msg += (
                f"Today's Plan ({request.planName}):\n"
                f"  Focus: {request.todayPlan.get('focus')}\n"
                f"  Exercises:\n"
            )
            for ex in request.todayPlan.get("exercises", []):
                user_msg += f"    - {ex.get('name')} ({ex.get('sets')} sets × {ex.get('reps')} reps)\n"

        user_msg += f"\nUser Message: \"{message}\""
>>>>>>> 12c61aafb90e4a90001d8632bfb95c95278aab20

        response = openai_client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": system_msg},
                {"role": "user", "content": user_msg},
            ],
            temperature=0.8,
        )
        reply = response.choices[0].message.content.strip()

        return {"success": True, "type": "chat", "reply": reply}

    except Exception as e:
        print("❌ CHAT ERROR:", str(e))
        return {"success": False, "error": str(e)}