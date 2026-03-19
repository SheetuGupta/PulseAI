# e:/videoAI/form_analysis/pipeline/feedback_builder.py
from models.schemas import FormFeedback, FormIssue, FrameAnalysis

def build_feedback(gemini_result: dict, frame_analyses: list[FrameAnalysis], video_duration: float) -> FormFeedback:
    frames_with_pose = [f for f in frame_analyses if f.pose_detected]
    
    issues = [FormIssue(**issue) for issue in gemini_result.get("issues", [])]
    
    return FormFeedback(
        exercise_detected=gemini_result.get("exercise_detected", "Unknown"),
        form_score=gemini_result.get("form_score", 5),
        is_correct_form=gemini_result.get("is_correct_form", False),
        is_wrong_exercise=gemini_result.get("is_wrong_exercise", False),
        suggested_regression=gemini_result.get("suggested_regression", ""),
        issues=issues,
        positive_observations=gemini_result.get("positive_observations", []),
        overall_summary=gemini_result.get("overall_summary", ""),
        priority_correction=gemini_result.get("priority_correction", ""),
        frame_count=len(frame_analyses),
        video_duration_seconds=video_duration
    )
