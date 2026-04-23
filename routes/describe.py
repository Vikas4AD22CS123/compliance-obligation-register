from flask import Blueprint, jsonify, request


# Blueprint keeps describe routes organized in one file
describe_bp = Blueprint("describe", __name__)


@describe_bp.route("/describe", methods=["POST"])
def describe():
    # Read JSON sent by the client
    data = request.get_json() or {}

    # Dummy response for Day 1 setup
    return jsonify({
        "message": "Describe endpoint is working",
        "input": data
    })
