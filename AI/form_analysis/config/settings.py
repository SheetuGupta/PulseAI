# form_analysis/config/settings.py
import os
from dotenv import load_dotenv
import pathlib
from openai import OpenAI

root_env = os.path.join(os.getcwd(), ".env")
load_dotenv(root_env, override=True)

OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY") or "UNSET_OPENAI_KEY"
print("FORM ANALYSIS KEY RESOLVED TO:", OPENAI_API_KEY)
PORT: int = int(os.getenv("PORT", 8001))
MAX_VIDEO_SECONDS: int = int(os.getenv("MAX_VIDEO_SECONDS", 30))
FRAMES_PER_SECOND: int = int(os.getenv("FRAMES_PER_SECOND", 1))

MODEL = "gpt-4o"

openai_client = OpenAI(api_key=OPENAI_API_KEY)
