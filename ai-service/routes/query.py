from flask import Blueprint, request, jsonify
from services.groq_client import call_groq
import chromadb

query_bp = Blueprint("query", __name__)

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
    data = request.json
    question = data.get("question", "")

    if not question:
        return jsonify({"error": "Question is required"}), 400

    # Step 1: Retrieve top 3 relevant docs
    results = collection.query(
        query_texts=[question],
        n_results=3
    )

    docs = results["documents"][0]
    ids = results["ids"][0]

    # Step 2: Build context
    context = "\n".join(docs)

    # Step 3: Ask AI using context
    prompt = f"""
Answer the question using the context below.

Context:
{context}

Question:
{question}

Rules:
- Answer directly (no role phrases like "as an assistant")
- Be clear and concise
- Use only the given context

Answer:
"""

    answer = call_groq(prompt)

    # Step 4: Return response
    return jsonify({
    "answer": answer,
    "sources": list(ids)
})