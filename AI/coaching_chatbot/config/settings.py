# coaching_chatbot/config/settings.py
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
DATABASE_URL = os.getenv("DATABASE_URL", "")
PORT = int(os.getenv("PORT", 8002))

MAX_HISTORY_MESSAGES = int(os.getenv("MAX_HISTORY_MESSAGES", 20))
MAX_MEMORY_CHUNKS = int(os.getenv("MAX_MEMORY_CHUNKS", 8))
MEMORY_IMPORTANCE_THRESHOLD = float(os.getenv("MEMORY_IMPORTANCE_THRESHOLD", 0.3))

gemini_client = genai.Client(api_key=GEMINI_API_KEY)
MODEL = "gemini-2.5-flash-lite"
EMBEDDING_MODEL = "gemini-embedding-001"
