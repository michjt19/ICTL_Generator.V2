
from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
import os
import json
from parser.parse_pdf_to_tasks import parse_task_from_pdf
from generate_docs.generate_word import generate_word
from generate_docs.generate_excel import generate_excel
from generate_docs.generate_pdf import generate_pdf
from generate_docs.generate_ppt import generate_ppt

app = Flask(__name__)
CORS(app)

LOG_FILE = "backend/logs/packet_log.json"
STP_DIR = "backend/static/STPs/"

@app.route("/api/task", methods=["GET"])
def get_task():
    task_code = request.args.get("code")
    if not task_code:
        return jsonify({"error": "Missing task code"}), 400
    task_data = parse_task_from_pdf(STP_DIR, task_code)
    return jsonify(task_data)

@app.route("/api/generate", methods=["POST"])
def generate_packet():
    data = request.json
    task = data.get("task")
    if not task:
        return jsonify({"error": "No task data provided"}), 400

    word_path = generate_word(task)
    excel_path = generate_excel(task)
    pdf_path = generate_pdf(task)
    ppt_path = generate_ppt(task)

    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "task_id": task.get("task_id"),
        "files": [word_path, excel_path, pdf_path, ppt_path]
    }

    with open(LOG_FILE, "r+") as f:
        logs = json.load(f)
        logs.append(log_entry)
        f.seek(0)
        json.dump(logs, f, indent=2)

    return jsonify({"status": "Packet generated", "log": log_entry})

@app.route("/api/logs", methods=["GET"])
def get_logs():
    with open(LOG_FILE) as f:
        return jsonify(json.load(f))

if __name__ == "__main__":
    app.run(debug=True)
