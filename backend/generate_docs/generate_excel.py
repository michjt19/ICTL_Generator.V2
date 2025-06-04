
import openpyxl
from pathlib import Path

def generate_excel(task):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Training Task"
    ws.append(["Task ID", "Content"])
    ws.append([task["task_id"], task["content"]])
    path = Path(f"backend/static/{task['task_id']}_packet.xlsx")
    wb.save(path)
    return str(path)
