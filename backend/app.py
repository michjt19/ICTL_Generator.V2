from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from datetime import datetime
import os
import json
import io
import zipfile

from generate_docs.generate_word import generate_word
from generate_docs.generate_pdf import generate_pdf
from generate_docs.generate_excel import generate_excel
from generate_docs.generate_ppt import generate_ppt

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend

# ------------------------------------
@app.route("/")
def index():
    return "✅ Flask backend is running!"

# ------------------------------------
@app.route("/api/task")
def get_task():
    code = request.args.get("code", "").strip()

    try:
        with open(os.path.join("data", "tasks.json"), "r") as f:
            tasks = json.load(f)

        matched = next((task for task in tasks if task["code"].lower() == code.lower()), None)
        if not matched:
            return jsonify({"error": f"Task code {code} not found."}), 404

        return jsonify(matched)

    except Exception as e:
            return jsonify({"error": str(e)}), 500

# ------------------------------------
@app.route("/api/tasks")
def get_all_tasks():
    try:
        with open(os.path.join("data", "tasks.json"), "r") as f:
            tasks = json.load(f)
        return jsonify(tasks)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ------------------------------------
@app.route("/api/generate", methods=["POST"])
def generate_packet():
    try:
        data = request.json
        task = data.get("task", {})
        task_code = task.get("code", "UNKNOWN")

        temp_dir = "temp"
        os.makedirs(temp_dir, exist_ok=True)

        word_path = os.path.join(temp_dir, f"{task_code}_packet.docx")
        pdf_path = os.path.join(temp_dir, f"{task_code}_packet.pdf")
        excel_path = os.path.join(temp_dir, f"{task_code}_tracker.xlsx")
        ppt_path = os.path.join(temp_dir, f"{task_code}_slides.pptx")

        generate_word(task, word_path)
        generate_pdf(task, pdf_path)
        generate_excel(task, excel_path)
        generate_ppt(task, ppt_path)

        memory_file = io.BytesIO()
        with zipfile.ZipFile(memory_file, 'w') as zf:
            for file_path in [word_path, pdf_path, excel_path, ppt_path]:
                filename = os.path.basename(file_path)
                zf.write(file_path, arcname=filename)

        memory_file.seek(0)

        for file in [word_path, pdf_path, excel_path, ppt_path]:
            os.remove(file)

        return send_file(
            memory_file,
            mimetype='application/zip',
            as_attachment=True,
            download_name=f"{task_code}_packet.zip"
        )
    
    except Exception as e:
        print("❌ Error during packet generation:", str(e))  # ADD THIS LINE
        return jsonify({"status": "error", "message": str(e)}), 500

# ------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
