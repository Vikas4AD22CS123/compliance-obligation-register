from flask import Blueprint, jsonify
import time
from services.chroma_client import ChromaClient

health_bp = Blueprint("health", __name__)

start_time = time.time()
response_times = []

chroma = ChromaClient()

@health_bp.route("/health", methods=["GET"])
def health():
    uptime = time.time() - start_time

    # avg response time
    avg_time = sum(response_times)/len(response_times) if response_times else 0

    # chroma doc count
    count = chroma.collection.count()

    return jsonify({
        "model": "llama3-8b",
        "avg_response_time": round(avg_time, 3),
        "chroma_docs": count,
        "uptime_seconds": round(uptime, 2),
        "cache": "not implemented"
    })