from flask import Flask
from dotenv import load_dotenv
load_dotenv()

from routes.categorise import categorise_bp
from routes.query import query_bp

app = Flask(__name__)   # ✅ create app first

app.register_blueprint(categorise_bp)
app.register_blueprint(query_bp)   # ✅ after app

if __name__ == "__main__":
    app.run(debug=True)