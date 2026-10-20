
import json
from pathlib import Path

import requests
import numpy as np

from dataset import documents


OLLAMA_URL = "http://localhost:11434"
EMBEDDING_MODEL = "nomic-embed-text"
LLM_MODEL = "llama3.2:3b"

CACHE_FILE = Path(__file__).parent / "knowledge_base.json"


def get_embedding(text):
    """Convert text into a numerical embedding using Ollama."""
    response = requests.post(
        f"{OLLAMA_URL}/api/embed",
        json={
            "model": EMBEDDING_MODEL,
            "input": text
        },
        timeout=120
    )

    response.raise_for_status()
    return response.json()["embeddings"][0]


def build_knowledge_base():
    """Embed every passage while preserving its topic."""
    knowledge_base = []

    for topic, passages in documents.items():
        for passage in passages:
            knowledge_base.append({
                "topic": topic,
                "text": passage,
                "embedding": get_embedding(passage)
            })

    return knowledge_base


def load_or_build_knowledge_base():
    """Load cached embeddings or create and save them."""
    if CACHE_FILE.exists():
        try:
            with CACHE_FILE.open("r", encoding="utf-8") as file:
                cached_data = json.load(file)

            # Reuse the cache only if it matches the current documents.
            expected = [
                {"topic": topic, "text": passage}
                for topic, passages in documents.items()
                for passage in passages
            ]

            cached_content = [
                {"topic": item["topic"], "text": item["text"]}
                for item in cached_data
            ]

            if (
                cached_content == expected
                and all(
                    isinstance(item.get("embedding"), list)
                    and len(item["embedding"]) == 768
                    for item in cached_data
                )
            ):
                print(f"Loaded {len(cached_data)} passages from cache.")
                return cached_data

            print("Knowledge base changed; rebuilding cache.")

        except (OSError, json.JSONDecodeError, KeyError, TypeError):
            print("Cache is invalid; rebuilding knowledge base.")

    print("Creating embeddings for OS documents...")
    knowledge_base = build_knowledge_base()

    temporary_file = CACHE_FILE.with_suffix(".tmp")

    with temporary_file.open("w", encoding="utf-8") as file:
        json.dump(knowledge_base, file)

    temporary_file.replace(CACHE_FILE)

    print(f"Saved {len(knowledge_base)} passages to {CACHE_FILE.name}.")
    return knowledge_base


def cosine_similarity(vector_a, vector_b):
    """Measure similarity between two embedding vectors."""
    a = np.array(vector_a)
    b = np.array(vector_b)

    denominator = np.linalg.norm(a) * np.linalg.norm(b)

    if denominator == 0:
        return 0.0

    return float(np.dot(a, b) / denominator)



def retrieve_documents(question, knowledge_base, top_k=3, threshold=0.60):
    """Retrieve relevant passages and reject weak matches."""
    question_embedding = get_embedding(question)
    scored_passages = []

    for passage in knowledge_base:
        score = cosine_similarity(
            question_embedding,
            passage["embedding"]
        )

        scored_passages.append({
            "topic": passage["topic"],
            "text": passage["text"],
            "score": score
        })

    scored_passages.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    # Reject the question if even the best passage is insufficiently relevant.
    if not scored_passages or scored_passages[0]["score"] < threshold:
        return []

    return scored_passages[:top_k]



def generate_answer(question, retrieved_passages):
    """Generate an answer grounded in retrieved OS passages."""
    context = "\n".join(
        f"- [{item['topic']}] {item['text']}"
        for item in retrieved_passages
    )

    prompt = f"""You are OSLabAI, an Operating Systems tutor.

Answer clearly and simply using the supplied context.
Do not claim that the context states something it does not.
If the context is insufficient, say so.
Do not invent source citations.

Context:
{context}

Student question:
{question}

Answer:"""

    response = requests.post(
        f"{OLLAMA_URL}/api/generate",
        json={
            "model": LLM_MODEL,
            "prompt": prompt,
            "stream": False,
            "options": {"temperature": 0.2}
        },
        timeout=180
    )

    response.raise_for_status()
    return response.json()["response"].strip()


_knowledge_base = None


def get_knowledge_base():
    """Load the knowledge base once per application process."""
    global _knowledge_base

    if _knowledge_base is None:
        _knowledge_base = load_or_build_knowledge_base()

    return _knowledge_base
