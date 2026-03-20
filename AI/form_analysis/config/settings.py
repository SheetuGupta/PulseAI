# e:/videoAI/form_analysis/config/settings.py
import os
from dotenv import load_dotenv
import pathlib
from google import genai

root_env = os.path.join(os.getcwd(), ".env")
load_dotenv(root_env, override=True)

GEMINI_API_KEY: str = os.getenv("GENAI_API_KEY") or os.getenv("GEMINI_API_KEY") or "UNSET_GEMINI_KEY"
print("FORM ANALYSIS KEY RESOLVED TO:", GEMINI_API_KEY)
PORT: int = int(os.getenv("PORT", 8001))
MAX_VIDEO_SECONDS: int = int(os.getenv("MAX_VIDEO_SECONDS", 30))
FRAMES_PER_SECOND: int = int(os.getenv("FRAMES_PER_SECOND", 1))

MODEL = "gemini-2.5-flash"

gemini_client = genai.Client(api_key=GEMINI_API_KEY)
