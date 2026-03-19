# e:/videoAI/form_analysis/models/schemas.py
from pydantic import BaseModel

class JointAngle(BaseModel):
    joint_name: str
    angle_degrees: float
    timestamp_seconds: float

class PoseLandmark(BaseModel):
    name: str
    x: float
    y: float
    z: float
    visibility: float

class FrameAnalysis(BaseModel):
    timestamp_seconds: float
    landmarks: list[PoseLandmark]
    joint_angles: list[JointAngle]
    pose_detected: bool

class FormIssue(BaseModel):
    timestamp_seconds: float
    joint_or_body_part: str
    observation: str
    correction_cue: str
    severity: str

class FormFeedback(BaseModel):
    exercise_detected: str
    form_score: int
    is_correct_form: bool
    is_wrong_exercise: bool
    suggested_regression: str
    issues: list[FormIssue]
    positive_observations: list[str]
    overall_summary: str
    priority_correction: str
    frame_count: int
    video_duration_seconds: float

class AnalyzeRequest(BaseModel):
    exercise_hint: str = ""
    perceived_difficulty: str = ""

class AnalyzeResponse(BaseModel):
    success: bool
    feedback: FormFeedback | None = None
    error: str | None = None
    processing_time_seconds: float
