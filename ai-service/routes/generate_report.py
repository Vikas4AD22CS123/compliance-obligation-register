from flask import Blueprint, request, jsonify
import threading
import time
import uuid

generate_report_bp = Blueprint("generate_report", __name__)

# Store job results
jobs = {}

def process_report(job_id, topic):

    # Simulate long AI processing
    time.sleep(10)

    report = f"Compliance report generated for: {topic}"

    jobs[job_id] = {
        "status": "completed",
        "report": report
    }

    # Simulated webhook
    print(f"\nWebhook Sent -> Job {job_id} completed")


@generate_report_bp.route("/generate-report", methods=["POST"])
def generate_report():

    data = request.json
    topic = data.get("topic", "")

    if not topic:
        return jsonify({"error": "Topic is required"}), 400

    # Create unique job id
    job_id = str(uuid.uuid4())

    jobs[job_id] = {
        "status": "processing"
    }

    # Start background thread
    thread = threading.Thread(
        target=process_report,
        args=(job_id, topic)
    )

    thread.start()

    return jsonify({
        "job_id": job_id,
        "status": "processing"
    })
@generate_report_bp.route("/job/<job_id>", methods=["GET"])
def get_job(job_id):

    job = jobs.get(job_id)

    if not job:
        return jsonify({"error": "Job not found"}), 404

    return jsonify(job)