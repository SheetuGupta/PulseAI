import google.generativeai as genai
from config.settings import EMBEDDING_MODEL

def embed(text: str) -> list[float]:
    result = genai.embed_content(
        model=EMBEDDING_MODEL,
        content=text
    )
    return result['embedding']

def embed_batch(texts: list[str]) -> list[list[float]]:
    return [embed(t) for t in texts]
