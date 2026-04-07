# AI/form_analysis/pipeline/openai_analyzer.py
import json
import base64
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
1. Verify if the user is actually doing the exercise they mentioned. Set "is_wrong_exercise" to true if they are doing a completely different exercise.
2. If they are doing the wrong exercise, kindly explain this in the "overall_summary".
3. If they rated the exercise as hard/difficult, or are struggling significantly with form, suggest an easier regression in "suggested_regression". Otherwise leave it empty.

Look for these common form issues:
- Knee valgus (knees caving inward)
- Forward lean — spine angle deviating from ideal
- Incomplete range of motion — joint angles not reaching exercise-specific targets
- Asymmetry — significant difference between left and right joint angles (more than 15 degrees)
- Elbow flare — shoulder angles outside normal range
- Hip hinge mechanics
- Ankle mobility

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
  "positive_observations": ["string", "string"],
  "overall_summary": "string (2-3 sentences)",
  "priority_correction": "string (one sentence, the single most important fix)"
}"""
    return prompt


def analyze_with_openai(frames: list[dict], frame_analyses: list[FrameAnalysis], exercise_hint: str = "", perceived_difficulty: str = "") -> dict:
    prompt = build_analysis_prompt(frame_analyses, exercise_hint, perceived_difficulty)

    # Build multimodal content: text prompt + base64 image frames
    content = [{"type": "text", "text": prompt}]

    frame_count = 0
    for frame in frames:
        if frame_count >= 10:  # GPT-4o handles up to ~10 images well per request
            break
        img = frame.get("image")
        if img is None:
            continue
        # img may be a PIL Image or raw bytes — encode to base64
        try:
            import io
            import PIL.Image
            if isinstance(img, PIL.Image.Image):
                buf = io.BytesIO()
                img.save(buf, format="JPEG")
                b64 = base64.b64encode(buf.getvalue()).decode("utf-8")
            else:
                b64 = base64.b64encode(img).decode("utf-8")
            content.append({
                "type": "image_url",
                "image_url": {"url": f"data:image/jpeg;base64,{b64}", "detail": "low"},
            })
            frame_count += 1
        except Exception as img_err:
            print(f"[FRAME ENCODE ERROR] {img_err}")
            continue

    try:
        response = openai_client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": content}],
            max_tokens=1500,
            temperature=0.3,
        )
        text = response.choices[0].message.content.strip()

        if text.startswith("```json"):
            text = text[7:]
        elif text.startswith("```"):
            text = text[3:]
        if text.endswith("```"):
            text = text[:-3]

        return json.loads(text.strip())
    except Exception as e:
        print(f"OpenAI analysis error: {str(e)}")
        return {
            "exercise_detected": "Unknown",
            "is_wrong_exercise": False,
            "form_score": 5,
            "is_correct_form": False,
            "suggested_regression": "",
            "issues": [],
            "positive_observations": [],
            "overall_summary": "Could not parse detailed analysis. Please try again.",
            "priority_correction": "Resubmit video for analysis.",
        }
