from reportlab.lib.pagesizes import letter

from reportlab.pdfgen import canvas


def generate_pdf(
    student_name,
    total,
    percentage,
    grade
):

    file_name = f"reports/{student_name}_report.pdf"

    pdf = canvas.Canvas(
        file_name,
        pagesize=letter
    )

    # TITLE
    pdf.setFont(
        "Helvetica-Bold",
        20
    )

    pdf.drawString(
        180,
        750,
        "Student Report Card"
    )

    # STUDENT NAME
    pdf.setFont(
        "Helvetica",
        14
    )

    pdf.drawString(
        100,
        680,
        f"Student Name: {student_name}"
    )

    # TOTAL
    pdf.drawString(
        100,
        640,
        f"Total Marks: {total}"
    )

    # PERCENTAGE
    pdf.drawString(
        100,
        600,
        f"Percentage: {percentage:.2f}%"
    )

    # GRADE
    pdf.drawString(
        100,
        560,
        f"Grade: {grade}"
    )

    pdf.save()

    print("PDF Generated Successfully")