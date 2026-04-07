<<<<<<< HEAD
# form_analysis/config/settings.py
import os
from dotenv import load_dotenv
import pathlib
import google.generativeai as genai
=======
# AI/form_analysis/config/settings.py
import os
from dotenv import load_dotenv
from openai import OpenAI
>>>>>>> 12c61aafb90e4a90001d8632bfb95c95278aab20

root_env = os.path.join(os.getcwd(), ".env")
load_dotenv(root_env, override=True)

<<<<<<< HEAD
GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY") or "UNSET_GEMINI_KEY"
print("FORM ANALYSIS KEY RESOLVED")
=======
OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
>>>>>>> 12c61aafb90e4a90001d8632bfb95c95278aab20
PORT: int = int(os.getenv("PORT", 8001))
MAX_VIDEO_SECONDS: int = int(os.getenv("MAX_VIDEO_SECONDS", 30))
FRAMES_PER_SECOND: int = int(os.getenv("FRAMES_PER_SECOND", 1))

<<<<<<< HEAD
MODEL = "gemini-1.5-pro"

genai.configure(api_key=GEMINI_API_KEY)
=======
# gpt-4o for vision (multimodal), gpt-4o-mini for text-only tasks
MODEL = "gpt-4o"

openai_client = OpenAI(api_key=OPENAI_API_KEY) if OPENAI_API_KEY else None
>>>>>>> 12c61aafb90e4a90001d8632bfb95c95278aab20
