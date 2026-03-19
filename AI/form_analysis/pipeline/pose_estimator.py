# e:/videoAI/form_analysis/pipeline/pose_estimator.py
import urllib.request
import os
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from PIL import Image

from AI.form_analysis.models.schemas import FrameAnalysis, PoseLandmark
from AI.form_analysis.pipeline.angle_calculator import calculate_angles
POSE_LANDMARK_NAMES = [
    "nose", "left_eye_inner", "left_eye",
    "left_eye_outer", "right_eye_inner", "right_eye",
    "right_eye_outer", "left_ear", "right_ear",
    "mouth_left", "mouth_right",
    "left_shoulder", "right_shoulder",
    "left_elbow", "right_elbow",
    "left_wrist", "right_wrist",
    "left_pinky", "right_pinky",
    "left_index", "right_index",
    "left_thumb", "right_thumb",
    "left_hip", "right_hip",
    "left_knee", "right_knee",
    "left_ankle", "right_ankle",
    "left_heel", "right_heel",
    "left_foot_index", "right_foot_index"
]

class PoseEstimator:
    def __init__(self):
        # MediaPipe 0.10+ new Tasks API requires a `.task` model file
        model_path = os.path.join(os.path.dirname(__file__), 'pose_landmarker.task')
        if not os.path.exists(model_path):
            print("Downloading MediaPipe Pose model... (this only happens once)")
            url = "https://storage.googleapis.com/mediapipe-models/pose_landmarker/pose_landmarker_lite/float16/latest/pose_landmarker_lite.task"
            urllib.request.urlretrieve(url, model_path)
        
        base_options = python.BaseOptions(model_asset_path=model_path)
        options = vision.PoseLandmarkerOptions(
            base_options=base_options,
            output_segmentation_masks=False
        )
        self.detector = vision.PoseLandmarker.create_from_options(options)

    def estimate(self, image: Image.Image, timestamp: float) -> FrameAnalysis:
        # Mediapipe Tasks API expects an mp.Image wrapper
        image_np = np.array(image.convert("RGB"))
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image_np)
        
        results = self.detector.detect(mp_image)
        
        if not results.pose_landmarks:
            return FrameAnalysis(
                timestamp_seconds=timestamp,
                landmarks=[],
                joint_angles=[],
                pose_detected=False
            )
            
        landmarks = []
        # We process the first detected person (index 0)
        for i, lm in enumerate(results.pose_landmarks[0]):
            if i < len(POSE_LANDMARK_NAMES):
                name = POSE_LANDMARK_NAMES[i]
                landmarks.append(PoseLandmark(
                    name=name,
                    x=lm.x,
                    y=lm.y,
                    z=lm.z,
                    visibility=lm.visibility if hasattr(lm, 'visibility') else 1.0
                ))
                
        joint_angles = calculate_angles(landmarks, timestamp)
        
        return FrameAnalysis(
            timestamp_seconds=timestamp,
            landmarks=landmarks,
            joint_angles=joint_angles,
            pose_detected=True
        )

    def close(self):
        self.detector.close()
