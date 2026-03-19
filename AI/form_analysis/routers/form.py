# e:/videoAI/form_analysis/form_pipeline.py

import time
from typing import Dict, Any

from AI.form_analysis.pipeline.video_processor import validate_video, extract_frames
from AI.form_analysis.pipeline.pose_estimator import PoseEstimator
from AI.form_analysis.pipeline.gemini_analyzer import analyze_with_gemini
from AI.form_analysis.pipeline.feedback_builder import build_feedback
from AI.form_analysis.config.settings import FRAMES_PER_SECOND
from AI.form_analysis.config.settings import MAX_VIDEO_SECONDS

def analyze_form_pipeline(
    video_bytes: bytes,
    exercise_hint: str = "",
    perceived_difficulty: str = ""
) -> Dict[str, Any]:

    start_time = time.time()

    try:
        # -------------------------------
        # 1. Validate Video
        # -------------------------------
        validation = validate_video(video_bytes)
        if not validation["valid"]:
            return {
                "success": False,
                "error": validation["error"],
                "processing_time_seconds": 0.0
            }

        # -------------------------------
        # 2. Extract Frames
        # -------------------------------
        frames = extract_frames(video_bytes, fps=FRAMES_PER_SECOND)
        if not frames:
            return {
                "success": False,
                "error": "Could not extract frames from video.",
                "processing_time_seconds": 0.0
            }

        # -------------------------------
        # 3. Pose Estimation
        # -------------------------------
        estimator = PoseEstimator()
        frame_analyses = []

        try:
            for frame in frames:
                analysis = estimator.estimate(frame["image"], frame["timestamp"])
                frame_analyses.append(analysis)
        finally:
            estimator.close()

        # -------------------------------
        # 4. Gemini Analysis
        # -------------------------------
        gemini_result = analyze_with_gemini(
            frames,
            frame_analyses,
            exercise_hint,
            perceived_difficulty
        )

        # -------------------------------
        # 5. Build Feedback
        # -------------------------------
        feedback = build_feedback(
            gemini_result,
            frame_analyses,
            validation["duration"]
        )

        processing_time = time.time() - start_time

        return {
            "success": True,
            "feedback": feedback,
            "processing_time_seconds": round(processing_time, 2)
        }

    except Exception as e:
        return {
            "success": False,
            "error": f"Analysis failed: {str(e)}",
            "processing_time_seconds": round(time.time() - start_time, 2)
        }