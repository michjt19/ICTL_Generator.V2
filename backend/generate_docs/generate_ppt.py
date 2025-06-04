
from pptx import Presentation
from pathlib import Path

def generate_ppt(task):
    prs = Presentation()
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    title = slide.shapes.title
    content = slide.placeholders[1]
    title.text = f"Task {task['task_id']}"
    content.text = task["content"]
    path = Path(f"backend/static/{task['task_id']}_packet.pptx")
    prs.save(path)
    return str(path)
