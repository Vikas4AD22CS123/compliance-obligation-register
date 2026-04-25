from flask import Blueprint, request, jsonify
from services.chroma_client import ChromaClient
from services.groq_client import GroqClient
from services.cache import get_cache_key, get_from_cache, set_cache
import time
from routes.health import response_times

query_bp = Blueprint("query", __name__)

chroma = ChromaClient()
groq = GroqClient()

@query_bp.route("/query", methods=["POST"])
def query():
    start = time.time()

    data = request.get_json()

    if not data or "question" not in data:
        return jsonify({"error": "Question is required"}), 400

    question = data["question"]

    # ✅ CACHE CHECK
    cache_key = get_cache_key(question)
    cached = get_from_cache(cache_key)
    if cached:
        return jsonify(cached)

    # 🔍 Step 1: Search docs
    results = chroma.query([question])
    docs = results["documents"][0]

    # 🧠 Step 2: Prompt
    context = "\n".join(docs)

    prompt = f"""
You are a compliance assistant.

Answer using ONLY the context.
- Keep answer short (1–2 lines)
- If not found, say "Not found in context"

Context:
{context}

Question:
{question}
"""

    # 🤖 Step 3: LLM
    answer = groq.generate([
        {"role": "user", "content": prompt}
    ])

    # ⏱️ TIME TRACKING
    end = time.time()
    response_times.append(end - start)

    if len(response_times) > 10:
        response_times.pop(0)

    # 📤 RESPONSE
    response = {
        "answer": answer,
        "sources": [] if answer.strip().lower().startswith("not found") else docs
    }

    # ✅ CACHE SAVE
    set_cache(cache_key, response)

    return jsonify(response)