# e:/videoAI/form_analysis/routers/form.py
import time
from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import JSONResponse
from models.schemas import AnalyzeResponse, FormFeedback
from pipeline.video_processor import validate_video, extract_frames
from pipeline.pose_estimator import PoseEstimator
from pipeline.gemini_analyzer import analyze_with_gemini
from pipeline.feedback_builder import build_feedback
from config.settings import FRAMES_PER_SECOND

router = APIRouter(prefix="/api/form", tags=["form"])

@router.post("/analyze", response_model=AnalyzeResponse)
async def analyze_form(
    video: UploadFile = File(...),
    exercise_hint: str = Form(default=""),
    perceived_difficulty: str = Form(default="")
):
    start_time = time.time()
    
    try:
        video_bytes = await video.read()
        
        validation = validate_video(video_bytes)
        if not validation["valid"]:
            return JSONResponse(
                status_code=400,
                content=AnalyzeResponse(
                    success=False,
                    error=validation["error"],
                    processing_time_seconds=0.0
                ).model_dump()
            )
            
        frames = extract_frames(video_bytes, fps=FRAMES_PER_SECOND)
        if not frames:
            return JSONResponse(
                status_code=422,
                content=AnalyzeResponse(
                    success=False,
                    error="Could not extract frames from video.",
                    processing_time_seconds=0.0
                ).model_dump()
            )
            
        estimator = PoseEstimator()
        frame_analyses = []
        try:
            for frame in frames:
                analysis = estimator.estimate(frame["image"], frame["timestamp"])
                frame_analyses.append(analysis)
        finally:
            estimator.close()
            
        gemini_result = analyze_with_gemini(frames, frame_analyses, exercise_hint, perceived_difficulty)
        
        feedback = build_feedback(gemini_result, frame_analyses, validation["duration"])
        
        processing_time = time.time() - start_time
        
        return AnalyzeResponse(
            success=True,
            feedback=feedback,
            processing_time_seconds=round(processing_time, 2)
        )
        
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content=AnalyzeResponse(
                success=False,
                error=f"Analysis failed: {str(e)}",
                processing_time_seconds=round(time.time() - start_time, 2)
            ).model_dump()
        )
