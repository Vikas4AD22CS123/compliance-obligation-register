from flask import Blueprint, request, jsonify
from services.chroma_client import ChromaClient
from services.groq_client import GroqClient

query_bp = Blueprint("query", __name__)

chroma = ChromaClient()
groq = GroqClient()

@query_bp.route("/query", methods=["POST"])
def query():
    data = request.get_json()

    if not data or "question" not in data:
        return jsonify({"error": "Question is required"}), 400

    question = data["question"]

    # 🔍 Step 1: Search top 3 docs
    results = chroma.query([question])
    docs = results["documents"][0]  # list of docs

    # 🧠 Step 2: Create prompt
    context = "\n".join(docs)

    prompt = f"""
    Answer the question using ONLY the context below.

    Context:
    {context}

    Question:
    {question}

    Give clear answer.
    """

    # 🤖 Step 3: Call Groq
    answer = groq.generate([
        {"role": "user", "content": prompt}
    ])

    # 📤 Step 4: Return
    return jsonify({
        "answer": answer,
        "sources": docs
    })