from flask import Blueprint, jsonify, request


# Blueprint keeps recommend routes organized in one file
recommend_bp = Blueprint("recommend", __name__)


@recommend_bp.route("/recommend", methods=["POST"])
def recommend():
    # Read JSON sent by the client
    data = request.get_json() or {}

    # Dummy response for Day 1 setup
    return jsonify({
        "message": "Recommend endpoint is working",
        "input": data
    })
