# coaching_chatbot/memory/embedder.py
from config.settings import gemini_client, EMBEDDING_MODEL

def embed(text: str) -> list[float]:
    result = gemini_client.models.embed_content(
        model=EMBEDDING_MODEL,
        contents=text
    )
    return result.embeddings[0].values

def embed_batch(texts: list[str]) -> list[list[float]]:
    return [embed(t) for t in texts]
