# coaching_chatbot/memory/embedder.py
from config.settings import openai_client, EMBEDDING_MODEL

def embed(text: str) -> list[float]:
    result = openai_client.embeddings.create(
        input=text,
        model=EMBEDDING_MODEL
    )
    return result.data[0].embedding

def embed_batch(texts: list[str]) -> list[list[float]]:
    return [embed(t) for t in texts]
