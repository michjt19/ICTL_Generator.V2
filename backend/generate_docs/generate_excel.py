import xlsxwriter

def generate_excel(task, filepath):
    workbook = xlsxwriter.Workbook(filepath)
    worksheet = workbook.add_worksheet("Task Tracker")

    bold = workbook.add_format({"bold": True})

    worksheet.write("A1", "Task Code", bold)
    worksheet.write("B1", task["code"])
    worksheet.write("A2", "Title", bold)
    worksheet.write("B2", task["title"])
    worksheet.write("A3", "Condition", bold)
    worksheet.write("B3", task["condition"])
    worksheet.write("A4", "Standard", bold)
    worksheet.write("B4", task["standard"])

    if "steps" in task:
        worksheet.write("A6", "Performance Steps", bold)
        for i, step in enumerate(task["steps"], start=7):
            worksheet.write(f"A{i}", f"Step {i - 6}")
            worksheet.write(f"B{i}", step)

    workbook.close()
