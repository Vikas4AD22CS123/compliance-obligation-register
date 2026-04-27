from flask import Flask, jsonify
from flask_cors import CORS

from routes.describe import describe_bp
from routes.recommend import recommend_bp
from routes.generate_report import report_bp
from routes.health import health_bp
from routes.analyse_document import analyse_bp


def create_app():
    # Create the Flask app
    app = Flask(__name__)

    # Allow requests from the frontend during development
    CORS(app)

    # Register route blueprints
    app.register_blueprint(describe_bp)
    app.register_blueprint(recommend_bp)
    app.register_blueprint(report_bp)
    app.register_blueprint(health_bp)
    app.register_blueprint(analyse_bp)

    @app.route("/health", methods=["GET"])
    def health():
        # Simple endpoint to check if the service is running
        return jsonify({"status": "ok"})

    return app


app = create_app()


if __name__ == "__main__":
    # Start the app in debug mode for local development
    app.run(debug=True)
