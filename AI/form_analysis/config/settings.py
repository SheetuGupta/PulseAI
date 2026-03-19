# e:/videoAI/form_analysis/config/settings.py
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
PORT: int = int(os.getenv("PORT", 8001))
MAX_VIDEO_SECONDS: int = int(os.getenv("MAX_VIDEO_SECONDS", 10))
FRAMES_PER_SECOND: int = int(os.getenv("FRAMES_PER_SECOND", 1))

MODEL = "gemini-2.5-flash"

gemini_client = genai.Client(api_key=GEMINI_API_KEY)
