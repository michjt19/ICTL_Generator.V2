from fpdf import FPDF

def generate_pdf(task, filepath):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, task["title"], ln=True)

    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, f"Task Code: {task['code']}", ln=True)
    pdf.multi_cell(0, 10, f"Condition: {task['condition']}")
    pdf.multi_cell(0, 10, f"Standard: {task['standard']}")

    if "steps" in task:
        pdf.set_font("Arial", "B", 14)
        pdf.cell(0, 10, "Performance Steps", ln=True)

        pdf.set_font("Arial", size=12)
        for i, step in enumerate(task["steps"], 1):
            pdf.multi_cell(0, 10, f"{i}. {step}")

    pdf.output(filepath)
