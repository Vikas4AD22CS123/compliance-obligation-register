from flask import Blueprint, request, jsonify
import threading
import uuid
import time

report_bp = Blueprint("report", __name__)

jobs = {}

def generate_report(job_id, question):
    time.sleep(5)
    jobs[job_id]["status"] = "completed"
    jobs[job_id]["result"] = f"Report for: {question}"

@report_bp.route("/generate-report", methods=["POST"])
def generate():
    data = request.get_json()
    question = data.get("question")

    job_id = str(uuid.uuid4())

    jobs[job_id] = {
        "status": "processing",
        "result": None
    }

    threading.Thread(target=generate_report, args=(job_id, question)).start()

    return jsonify({
        "job_id": job_id,
        "status": "processing"
    })

@report_bp.route("/report-status/<job_id>", methods=["GET"])
def status(job_id):
    job = jobs.get(job_id)

    if not job:
        return jsonify({"error": "Invalid job_id"}), 404

    return jsonify(job)