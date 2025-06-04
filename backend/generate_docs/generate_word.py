
from docx import Document
from pathlib import Path

def generate_word(task):
    doc = Document()
    doc.add_heading(f"Training Packet for {task['task_id']}", 0)
    doc.add_paragraph(task['content'])
    path = Path(f"backend/static/{task['task_id']}_packet.docx")
    doc.save(path)
    return str(path)
