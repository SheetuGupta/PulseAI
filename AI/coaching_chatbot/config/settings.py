# AI/coaching_chatbot/config/settings.py
import os
from dotenv import load_dotenv
<<<<<<< HEAD
import pathlib
import google.generativeai as genai
=======
from openai import OpenAI
>>>>>>> 12c61aafb90e4a90001d8632bfb95c95278aab20

root_env = os.path.join(os.getcwd(), ".env")
load_dotenv(root_env, override=True)

<<<<<<< HEAD
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") or "UNSET_GEMINI_KEY"
=======
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
>>>>>>> 12c61aafb90e4a90001d8632bfb95c95278aab20
DATABASE_URL = os.getenv("DATABASE_URL", "")
PORT = int(os.getenv("PORT", 8002))

MAX_HISTORY_MESSAGES = int(os.getenv("MAX_HISTORY_MESSAGES", 20))
MAX_MEMORY_CHUNKS = int(os.getenv("MAX_MEMORY_CHUNKS", 8))
MEMORY_IMPORTANCE_THRESHOLD = float(os.getenv("MEMORY_IMPORTANCE_THRESHOLD", 0.3))

<<<<<<< HEAD
genai.configure(api_key=GEMINI_API_KEY)
MODEL = "gemini-1.5-flash"
EMBEDDING_MODEL = "models/text-embedding-004"
=======
openai_client = OpenAI(api_key=OPENAI_API_KEY)
MODEL = "gpt-4o-mini"
EMBEDDING_MODEL = "text-embedding-3-small"
>>>>>>> 12c61aafb90e4a90001d8632bfb95c95278aab20
