
import re
import os
from PyPDF2 import PdfReader

def parse_task_from_pdf(directory, task_code):
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            path = os.path.join(directory, filename)
            reader = PdfReader(path)
            for page in reader.pages:
                text = page.extract_text()
                if task_code in text:
                    match = re.search(rf"({task_code}.*?)\n(?=\d{{3}}-\d{{3}}-\d{{4}}|$)", text, re.DOTALL)
                    if match:
                        return {"task_id": task_code, "content": match.group(1)}
    return {"error": "Task not found"}
