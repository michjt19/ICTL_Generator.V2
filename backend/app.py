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

# ------------------------------------
# ✅ GET route to fetch task info
@app.route("/api/task")
def get_task():
    code = request.args.get("code")

    # Simulated task data — eventually will pull from STP JSON
    task_data = {
        "code": code,
        "title": "Simulated Task Title",
        "condition": "Given necessary equipment and a training environment...",
        "standard": "Complete task IAW Army standards with zero critical errors.",
        "steps": [
            "Step 1: Do something",
            "Step 2: Do something else",
        ]
    }

    return jsonify(task_data)

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
