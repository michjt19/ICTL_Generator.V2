
from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas
from pathlib import Path

def generate_pdf(task):
    path = Path(f"backend/static/{task['task_id']}_packet.pdf")
    c = canvas.Canvas(str(path), pagesize=LETTER)
    c.setFont("Helvetica", 12)
    c.drawString(100, 750, f"Training Packet for {task['task_id']}")
    y = 730
    for line in task["content"].split("\n"):
        if y < 50:
            c.showPage()
            y = 750
        c.drawString(50, y, line.strip())
        y -= 20
    c.save()
    return str(path)
