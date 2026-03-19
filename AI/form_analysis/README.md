# PulseAI — Form Analysis Module

This is a standalone, stateless FastAPI microservice that analyzes exercise form from a short video (up to 30s) using **MediaPipe Tasks API (Pose estimation)** and **Google Gemini 2.5 Flash Vision**. It returns timestamped coaching feedback as JSON.

---

## 💻 For Backend Engineers

This module is designed to run completely independently from your main application server. Your main server just acts as a securely authenticated proxy/caller to this module.

### How to Run Locally
1. Clone this repository.
2. `cp .env.example .env` and add your `GEMINI_API_KEY`.
3. Install dependencies: `pip install -r requirements.txt`. (Requires Python 3.11+)
4. Run the server: `uvicorn main:app --reload --port 8001`.
5. *Note: Local testing requires `ffmpeg` installed on your system (`winget install gyan.ffmpeg` for Windows, `brew install ffmpeg` for Mac).*

### API Contract

**`POST /api/form/analyze`**

**Request (multipart/form-data):**
- `video`: file (mp4, mov, avi, webm, mp3)
- `exercise_hint`: string (optional, e.g. "squat")
- `perceived_difficulty`: string (optional, e.g. "hard")

**Response (JSON):**
```json
{
  "success": true,
  "feedback": {
    "exercise_detected": "squat",
    "form_score": 6,
    "is_correct_form": false,
    "is_wrong_exercise": false,
    "suggested_regression": "Try box squats to build confidence with depth",
    "issues": [
      {
        "timestamp_seconds": 3.0,
        "joint_or_body_part": "left knee",
        "observation": "Knee angle tracking inside of foot",
        "correction_cue": "Push your left knee out toward your pinky toe",
        "severity": "moderate"
      }
    ],
    "positive_observations": [
      "Good depth achieved at bottom position",
      "Spine maintained neutral throughout"
    ],
    "overall_summary": "Your squat shows good depth but left knee valgus is a recurring issue. Focus on knee tracking before adding weight.",
    "priority_correction": "Drive your left knee outward to track over your pinky toe throughout the entire movement.",
    "frame_count": 10,
    "video_duration_seconds": 9.8
  },
  "processing_time_seconds": 4.2
}
```

### Proxy Example (Python backend to this microservice)
Your main application should ideally call this Python code snippet anytime an authenticated user uploads a video:
```python
import requests

def analyze_form(video_bytes: bytes, exercise_hint: str = "", perceived_difficulty: str = "") -> dict:
    response = requests.post(
        "https://your-form-module.onrender.com/api/form/analyze",
        files={"video": ("video.mp4", video_bytes, "video/mp4")},
        data={"exercise_hint": exercise_hint, "perceived_difficulty": perceived_difficulty},
        timeout=60
    )
    return response.json()
```

### Deployment (Render Free Tier)
1. Push this code to a GitHub repo.
2. Create Web Service on Render.
3. Build Command: `apt-get install -y ffmpeg && pip install -r requirements.txt`
4. Start Command: `uvicorn main:app --host 0.0.0.0 --port 10000`
5. Add configuration environment variable: `GEMINI_API_KEY`.

---

## 🎨 For Frontend Engineers

Your frontend application **should never call this module directly**! Doing so would permanently expose the API URL to the public, completely bypassing your main user authentication.

**The architecture flow is:**
1. Next.js/React securely uploads the user's video to your **Main Backend API**.
2. Main Backend verifies the user, and silently calls this **Form Analysis API**.
3. Main Backend returns the structured JSON to you.
4. You render the beautiful coaching UI.

### Testing the Module Yourself
We built a simple testing UI strictly for frontend engineers to view the JSON output that they will eventually work with.

Simply double-click and open `test_client.html` in your browser. As long as the backend engineer has the local Python server running at `http://localhost:8001`, you can upload videos right from your browser and view the exact JSON payload the backend will return! Try playing with different videos to visualize the data shape.

### Example Frontend Integration (Next.js)
```tsx
async function uploadAndAnalyze(file: File, hint: string, difficulty: string) {
  const formData = new FormData();
  formData.append('video', file);
  formData.append('exercise_hint', hint);
  formData.append('perceived_difficulty', difficulty);

  // Call YOUR secure MAIN BACKEND, not our Form Module directly.
  const res = await fetch('/api/user/analyze-video', {
    method: 'POST',
    body: formData
  });

  const data = await res.json();
  
  if (data.feedback.is_wrong_exercise) {
     alert(`Oops, you're not doing a ${hint}! The AI thinks you are doing a ${data.feedback.exercise_detected}.`);
  } else if (data.feedback.suggested_regression) {
     toast(`Struggling? Let's fix that: ${data.feedback.suggested_regression}`);
  }

  return data.feedback.issues; // Array of timestamped cues to map over
}
```

---

## 🧠 Under the Hood (How it works natively)

If you're curious about the mechanics of the pipeline:
1. **Validation**: Subprocess `ffmpeg.probe` ensures the video is under 30 seconds.
2. **Extraction**: `ffmpeg.input` pulls exactly 1 frame per second.
3. **Computer Vision**: Google MediaPipe (Tasks API) maps 33 physical joints on the human body on every frame.
4. **Calculus**: We calculate 10 multi-dimensional joint vectors (knees, hips, spine, shoulders) on each identified pose.
5. **Generative AI**: The frames + angle metadata are asynchronously bundled and sent to **Gemini 2.5 Flash**, which cross-references fitness rules (`exercise_rules.json`) to generate a personalized algorithmic coaching cue.
