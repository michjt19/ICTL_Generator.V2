from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes (frontend can access backend)

# ------------------------------------
# ✅ Root route (just confirms backend is running)
@app.route("/")
def index():
    return "✅ Flask backend is running!"

import json
import os

# ------------------------------------
# ✅ GET route to fetch real task info from JSON
@app.route("/api/task")
def get_task():
    code = request.args.get("code")
    filepath = os.path.join(os.path.dirname(__file__), "data", "tasks.json")

    try:
        with open(filepath, "r") as f:
            tasks = json.load(f)

        for task in tasks:
            if task["code"] == code:
                return jsonify(task)

        return jsonify({"error": "Task not found"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ------------------------------------
# ✅ POST route to simulate packet generation
@app.route("/api/generate", methods=["POST"])
def generate_packet():
    try:
        data = request.json
        task = data.get("task", {})
        task_code = task.get("code", "UNKNOWN")
        training_time = datetime.utcnow().isoformat()

        print(f"[{training_time}] Packet generation requested for task {task_code}")

        # Simulated response — later will return actual file/zip
        return jsonify({
            "status": "success",
            "message": f"Packet generated for task {task_code}",
            "timestamp": training_time
        })

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# ------------------------------------
# ✅ Run Flask development server
if __name__ == "__main__":
    app.run(debug=True)
