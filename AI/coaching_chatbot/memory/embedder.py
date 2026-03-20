# coaching_chatbot/memory/embedder.py
from config.settings import openai_client, EMBEDDING_MODEL


def embed(text: str) -> list[float]:
    result = openai_client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=text,
    )
    return result.data[0].embedding


def embed_batch(texts: list[str]) -> list[list[float]]:
    result = openai_client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=texts,
    )
    return [item.embedding for item in result.data]
