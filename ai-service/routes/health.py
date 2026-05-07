from flask import Blueprint, jsonify
import chromadb
import time

health_bp = Blueprint("health", __name__)

# Start time when server starts
start_time = time.time()

# Fake response times list (you can improve later)
response_times = [1.1, 1.3, 1.0, 1.2]

# Fake cache stats
cache_hits = 5
cache_misses = 2

# ChromaDB setup
client = chromadb.Client(
    chromadb.config.Settings(
        persist_directory="./chroma_data"
    )
)

collection = client.get_or_create_collection(name="compliance_docs")


@health_bp.route("/health", methods=["GET"])
def health():

    uptime = round(time.time() - start_time, 2)

    avg_response_time = round(
        sum(response_times) / len(response_times), 2
    )

    return jsonify({
        "model": "llama-3.3-70b-versatile",
        "avg_response_time": avg_response_time,
        "chromadb_doc_count": collection.count(),
        "uptime_seconds": uptime,
        "cache_hits": cache_hits,
        "cache_misses": cache_misses
    })