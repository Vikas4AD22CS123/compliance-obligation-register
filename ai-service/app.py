from flask import Flask
from routes.categorise import categorise_bp
from routes.query import query_bp

app = Flask(__name__)
app.register_blueprint(query_bp)

# register route
app.register_blueprint(categorise_bp)

@app.route("/")
def home():
    return {"message": "AI Service Running"}

if __name__ == "__main__":
    app.run(port=5000, debug=True)