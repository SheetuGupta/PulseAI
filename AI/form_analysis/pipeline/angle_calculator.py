# e:/videoAI/form_analysis/pipeline/angle_calculator.py
import numpy as np
from models.schemas import PoseLandmark, JointAngle

def calculate_angle(a: tuple[float, float], b: tuple[float, float], c: tuple[float, float]) -> float:
    a_np = np.array(a)
    b_np = np.array(b)
    c_np = np.array(c)
    
    vector_ba = a_np - b_np
    vector_bc = c_np - b_np
    
    norm_ba = np.linalg.norm(vector_ba)
    norm_bc = np.linalg.norm(vector_bc)
    
    if norm_ba == 0 or norm_bc == 0:
        return 0.0
        
    cosine = np.dot(vector_ba, vector_bc) / (norm_ba * norm_bc)
    angle = np.degrees(np.arccos(np.clip(cosine, -1.0, 1.0)))
    
    return float(angle)

def calculate_angles(landmarks: list[PoseLandmark], timestamp: float) -> list[JointAngle]:
    lm_dict = {lm.name: (lm.x, lm.y) for lm in landmarks}
    
    def get_pt(name):
        return lm_dict.get(name, (0.0, 0.0))
        
    angles_to_calc = [
        ("LEFT_KNEE_ANGLE", get_pt("left_hip"), get_pt("left_knee"), get_pt("left_ankle")),
        ("RIGHT_KNEE_ANGLE", get_pt("right_hip"), get_pt("right_knee"), get_pt("right_ankle")),
        ("LEFT_HIP_ANGLE", get_pt("left_shoulder"), get_pt("left_hip"), get_pt("left_knee")),
        ("RIGHT_HIP_ANGLE", get_pt("right_shoulder"), get_pt("right_hip"), get_pt("right_knee")),
        ("LEFT_ELBOW_ANGLE", get_pt("left_shoulder"), get_pt("left_elbow"), get_pt("left_wrist")),
        ("RIGHT_ELBOW_ANGLE", get_pt("right_shoulder"), get_pt("right_elbow"), get_pt("right_wrist")),
        ("LEFT_SHOULDER_ANGLE", get_pt("left_elbow"), get_pt("left_shoulder"), get_pt("left_hip")),
        ("RIGHT_SHOULDER_ANGLE", get_pt("right_elbow"), get_pt("right_shoulder"), get_pt("right_hip")),
        ("ANKLE_DORSIFLEXION_LEFT", get_pt("left_knee"), get_pt("left_ankle"), get_pt("left_foot_index")),
        ("ANKLE_DORSIFLEXION_RIGHT", get_pt("right_knee"), get_pt("right_ankle"), get_pt("right_foot_index")),
    ]
    
    joint_angles = []
    for name, p1, p2, p3 in angles_to_calc:
        angle_val = calculate_angle(p1, p2, p3)
        joint_angles.append(JointAngle(
            joint_name=name,
            angle_degrees=angle_val,
            timestamp_seconds=timestamp
        ))
        
    left_shoulder = get_pt("left_shoulder")
    right_shoulder = get_pt("right_shoulder")
    left_hip = get_pt("left_hip")
    right_hip = get_pt("right_hip")
    left_knee = get_pt("left_knee")
    right_knee = get_pt("right_knee")
    
    mid_shoulder = ((left_shoulder[0] + right_shoulder[0]) / 2.0, (left_shoulder[1] + right_shoulder[1]) / 2.0)
    mid_hip = ((left_hip[0] + right_hip[0]) / 2.0, (left_hip[1] + right_hip[1]) / 2.0)
    mid_knee = ((left_knee[0] + right_knee[0]) / 2.0, (left_knee[1] + right_knee[1]) / 2.0)
    
    spine_angle_val = calculate_angle(mid_shoulder, mid_hip, mid_knee)
    joint_angles.append(JointAngle(
        joint_name="SPINE_ANGLE",
        angle_degrees=spine_angle_val,
        timestamp_seconds=timestamp
    ))
    
    return joint_angles
