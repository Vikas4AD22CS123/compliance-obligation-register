from flask import Blueprint, request, jsonify
from services.groq_client import call_groq
import json

categorise_bp = Blueprint("categorise", __name__)

@categorise_bp.route("/categorise", methods=["POST"])
def categorise():
    data = request.json
    text = data.get("text", "")

    # Input validation
    if not text:
        return jsonify({"error": "Text is required"}), 400

    # Prompt
    prompt = f"""
You are a compliance expert.

Classify the given text into ONE of these categories:
Legal, Financial, Operational, Environmental

Text: {text}

IMPORTANT:
- Respond ONLY in valid JSON
- Do NOT add explanation outside JSON
- Do NOT use backticks
- Do NOT write anything else

Format:
{{
    "category": "Environmental",
    "confidence": 0.0,
    "reasoning": "short explanation"
}}
"""

    result = call_groq(prompt)

    # Convert AI string → JSON
    try:
        parsed = json.loads(result)
    except:
        parsed = {
            "category": "Unknown",
            "confidence": 0.0,
            "reasoning": "AI response parsing failed"
        }

    # FINAL RESPONSE (IMPORTANT)
    return jsonify(parsed)