from flask import Flask
from dotenv import load_dotenv
load_dotenv()

from routes.categorise import categorise_bp
from routes.query import query_bp
from routes.health import health_bp
from routes.report import report_bp

app = Flask(__name__)   # FIRST create app

app.register_blueprint(categorise_bp)
app.register_blueprint(query_bp)
app.register_blueprint(health_bp)   # AFTER app
app.register_blueprint(report_bp)

if __name__ == "__main__":
    app.run(debug=True)