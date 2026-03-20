# AI/form_analysis/config/settings.py
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
PORT: int = int(os.getenv("PORT", 8001))
MAX_VIDEO_SECONDS: int = int(os.getenv("MAX_VIDEO_SECONDS", 30))
FRAMES_PER_SECOND: int = int(os.getenv("FRAMES_PER_SECOND", 1))

# gpt-4o for vision (multimodal), gpt-4o-mini for text-only tasks
MODEL = "gpt-4o"

openai_client = OpenAI(api_key=OPENAI_API_KEY) if OPENAI_API_KEY else None
