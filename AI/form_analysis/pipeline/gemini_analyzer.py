# e:/videoAI/form_analysis/pipeline/gemini_analyzer.py
import json
import base64
from io import BytesIO
import PIL.Image
from AI.form_analysis.config.settings import openai_client, MODEL
from AI.form_analysis.models.schemas import FrameAnalysis

def build_analysis_prompt(frame_analyses: list[FrameAnalysis], exercise_hint: str = "", perceived_difficulty: str = "") -> str:
    frame_count = len([f for f in frame_analyses if f.pose_detected])
    duration = max([f.timestamp_seconds for f in frame_analyses]) if frame_analyses else 0.0
    
    prompt = f"You are an expert fitness coach and movement specialist. You are analyzing {frame_count} frames from a {duration}-second exercise video.\n\n"
    
    if exercise_hint:
        prompt += f"The user thinks they are performing: {exercise_hint}\n\n"
    else:
        prompt += "First identify what exercise the user is performing.\n\n"
        
    if perceived_difficulty:
        prompt += f"The user rated the difficulty of this exercise as: '{perceived_difficulty}'.\n\n"
        
    prompt += "POSE DATA FROM MEDIAPIPE:\n"
    
    for f in frame_analyses:
        if f.pose_detected:
            prompt += f"Frame at {f.timestamp_seconds}s:\n"
            for angle in f.joint_angles:
                prompt += f"  - {angle.joint_name}: {angle.angle_degrees:.1f}°\n"
            prompt += "\n"
            
    prompt += """YOUR TASK:
Analyze the exercise form based on both the visual frames and the pose angle data above.

Additional instructions:
1. Verify if the user is actually doing the exercise they mentioned. Set "is_wrong_exercise" to true if they are doing a completely different exercise layout than intended.
2. If they are doing the wrong exercise, kindly explain this in the "overall_summary".
3. If they rated the exercise as hard/difficult, or they are struggling significantly with form, suggest an easier regression/variation in "suggested_regression". Otherwise leave it empty.

Look for these common form issues:
- Knee valgus (knees caving inward) — knee angle asymmetry or knees tracking inside of feet
- Forward lean — spine angle deviating from ideal
- Incomplete range of motion — joint angles not reaching exercise-specific targets
- Asymmetry — significant difference between left and right joint angles (more than 15 degrees)
- Elbow flare — shoulder angles outside normal range
- Hip hinge mechanics — hip angle during hinge movements
- Ankle mobility — dorsiflexion limitations

RETURN ONLY VALID JSON. No markdown. No backticks. No explanation outside the JSON.

Use exactly this structure:
{
  "exercise_detected": "string",
  "is_wrong_exercise": boolean,
  "form_score": integer (1 to 10),
  "is_correct_form": boolean (true if score >= 7),
  "suggested_regression": "string (easier variation if struggling, else empty string)",
  "issues": [
    {
      "timestamp_seconds": number,
      "joint_or_body_part": "string",
      "observation": "string",
      "correction_cue": "string",
      "severity": "minor" or "moderate" or "critical"
    }
  ],
  "positive_observations": [
    "string", "string"
  ],
  "overall_summary": "string (2-3 sentences)",
  "priority_correction": "string (one sentence, the single most important fix)"
}

Be specific. Reference the actual angles from the pose data. A good correction cue sounds like a real coach: 'At 3 seconds, your left knee collapsed inward to 142 degrees — push your knees out toward your pinky toes on the way down.'"""

    return prompt

def analyze_with_gemini(frames: list[dict], frame_analyses: list[FrameAnalysis], exercise_hint: str = "", perceived_difficulty: str = "") -> dict:
    prompt = build_analysis_prompt(frame_analyses, exercise_hint, perceived_difficulty)
    
    content = [{"type": "text", "text": prompt}]
    
    frame_count = 0
    for frame in frames:
        if frame_count >= 30:
            break
            
        buffered = BytesIO()
        frame["image"].save(buffered, format="JPEG")
        base64_img = base64.b64encode(buffered.getvalue()).decode("utf-8")
        
        content.append({
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_img}",
                "detail": "low"
            }
        })
        frame_count += 1
        
    try:
        response = openai_client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": content}]
        )
        text = response.choices[0].message.content.strip()
        
        if text.startswith("```json"):
            text = text[7:]
        elif text.startswith("```"):
            text = text[3:]
            
        if text.endswith("```"):
            text = text[:-3]
            
        text = text.strip()
        return json.loads(text)
    except Exception as e:
        print(f"Gemini analysis error: {str(e)}")
        return {
            "exercise_detected": "Unknown",
            "is_wrong_exercise": False,
            "form_score": 5,
            "is_correct_form": False,
            "suggested_regression": "",
            "issues": [],
            "positive_observations": [],
            "overall_summary": "Could not parse detailed analysis. Please try again.",
            "priority_correction": "Resubmit video for analysis."
        }
