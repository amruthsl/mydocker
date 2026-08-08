from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1 style='color: green;'>Hello All!</h1>
    <p>Your Jenkins + Docker CI/CD pipeline is working perfectly.</p>
    <p>Every commit will now auto‑deploy.</p>
    """

@app.route("/api/info")
def info():
    return jsonify({
        "status": "success",
        "message": "CI/CD pipeline is running",
        "author": "amruth"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
