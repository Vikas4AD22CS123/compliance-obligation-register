from flask import Blueprint, request, jsonify
from services.groq_client import call_groq
from flask import Blueprint, request, jsonify
import chromadb
import time

query_bp = Blueprint("query", __name__)

from services.cache import (
    get_cached_response,
    save_to_cache
)

# Setup ChromaDB client
client = chromadb.Client(
    chromadb.config.Settings(
        persist_directory="./chroma_data"
    )
)

collection = client.get_or_create_collection(name="compliance_docs")

if collection.count() == 0:
    collection.add(
        documents=[
            "Company must follow environmental safety rules",
            "Financial audits must be conducted annually",
            "Employee attendance must be tracked daily"
        ],
        ids=["doc1", "doc2", "doc3"]
    )


@query_bp.route("/query", methods=["POST"])
def query():

    start_time = time.time()

    data = request.json
    question = data.get("question", "")

    if not question:
        return jsonify({"error": "Question is required"}), 400

    fresh = data.get("fresh", False)

    # Use cache unless fresh request
    if not fresh:
        cached = get_cached_response(question)

        if cached:
            cached["meta"]["cached"] = True
            return jsonify(cached)

    # Retrieve top 3 docs
    results = collection.query(
        query_texts=[question],
        n_results=3
    )

    docs = results["documents"][0]
    ids = results["ids"][0]

    # Build context
    context = "\n".join(docs)

    prompt = f"""
Answer ONLY using the provided context.

Context:
{context}

Question:
{question}

Rules:
- Keep answer short and direct
- Do not add extra explanations
- Do not invent information
- Use only the context

Answer:
"""

    answer = call_groq(prompt)

    response_time = round((time.time() - start_time) * 1000, 2)

    response_data = {
        "answer": answer,
        "sources": list(ids),
        "meta": {
            "confidence": 0.95,
            "model_used": "llama-3.3-70b-versatile",
            "tokens_used": len(answer.split()),
            "response_time_ms": response_time,
            "cached": False
        }
    }

    save_to_cache(question, response_data)

    return jsonify(response_data)