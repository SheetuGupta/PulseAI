<<<<<<< HEAD
import google.generativeai as genai
from config.settings import EMBEDDING_MODEL

def embed(text: str) -> list[float]:
    result = genai.embed_content(
        model=EMBEDDING_MODEL,
        content=text
    )
    return result['embedding']
=======
# coaching_chatbot/memory/embedder.py
from config.settings import openai_client, EMBEDDING_MODEL


def embed(text: str) -> list[float]:
    result = openai_client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=text,
    )
    return result.data[0].embedding

>>>>>>> 12c61aafb90e4a90001d8632bfb95c95278aab20

def embed_batch(texts: list[str]) -> list[list[float]]:
    result = openai_client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=texts,
    )
    return [item.embedding for item in result.data]
