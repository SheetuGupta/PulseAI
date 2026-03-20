# AI/coaching_chatbot/config/settings.py
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
DATABASE_URL = os.getenv("DATABASE_URL", "")
PORT = int(os.getenv("PORT", 8002))

MAX_HISTORY_MESSAGES = int(os.getenv("MAX_HISTORY_MESSAGES", 20))
MAX_MEMORY_CHUNKS = int(os.getenv("MAX_MEMORY_CHUNKS", 8))
MEMORY_IMPORTANCE_THRESHOLD = float(os.getenv("MEMORY_IMPORTANCE_THRESHOLD", 0.3))

openai_client = OpenAI(api_key=OPENAI_API_KEY)
MODEL = "gpt-4o-mini"
EMBEDDING_MODEL = "text-embedding-3-small"
