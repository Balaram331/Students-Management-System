import tkinter as tk

from tkinter import ttk, messagebox

from services.student_service import get_all_students

from services.result_service import calculate_result

from reports.pdf_generator import generate_pdf


def open_result_page():

    # CREATE WINDOW
    window = tk.Toplevel()

    window.title(
        "Result Management"
    )

    window.geometry("500x500")

    # STUDENT LABEL
    student_label = tk.Label(
        window,
        text="Select Student",
        font=("Arial", 14)
    )

    student_label.pack(pady=10)

    # GET STUDENTS
    students = get_all_students()

    student_names = []

    for student in students:

        student_names.append(
            f"{student[0]} - {student[1]}"
        )

    # STUDENT DROPDOWN
    student_combobox = ttk.Combobox(
        window,
        values=student_names,
        state="readonly",
        width=35
    )

    student_combobox.pack(pady=10)

    # TOTAL LABEL
    total_label = tk.Label(
        window,
        text="Total Marks:",
        font=("Arial", 14)
    )

    total_label.pack(pady=10)

    # PERCENTAGE LABEL
    percentage_label = tk.Label(
        window,
        text="Percentage:",
        font=("Arial", 14)
    )

    percentage_label.pack(pady=10)

    # GRADE LABEL
    grade_label = tk.Label(
        window,
        text="Grade:",
        font=("Arial", 14)
    )

    grade_label.pack(pady=10)

    # GENERATE RESULT FUNCTION
    def generate_result():

        student_value = (
            student_combobox.get()
        )

        # VALIDATION
        if not student_value:

            messagebox.showwarning(
                "Warning",
                "Please select student"
            )

            return

        # EXTRACT STUDENT ID
        student_id = (
            student_value.split(" - ")[0]
        )

        # GET RESULT FROM BACKEND
        total, percentage, grade = (
            calculate_result(student_id)
        )

        # UPDATE LABELS
        total_label.config(
            text=f"Total Marks: {total}"
        )

        percentage_label.config(
            text=f"Percentage: {percentage:.2f}%"
        )

        grade_label.config(
            text=f"Grade: {grade}"
        )

    # PDF GENERATION FUNCTION
    def generate_report_pdf():

        student_value = (
            student_combobox.get()
        )

        # VALIDATION
        if not student_value:

            messagebox.showwarning(
                "Warning",
                "Please select student"
            )

            return

        # EXTRACT STUDENT DATA
        student_id = (
            student_value.split(" - ")[0]
        )

        student_name = (
            student_value.split(" - ")[1]
        )

        # GET RESULT DATA
        total, percentage, grade = (
            calculate_result(student_id)
        )

        # GENERATE PDF
        generate_pdf(
            student_name,
            total,
            percentage,
            grade
        )

        messagebox.showinfo(
            "Success",
            "PDF Report Generated Successfully"
        )

    # GENERATE RESULT BUTTON
    generate_button = tk.Button(
        window,
        text="Generate Result",
        width=20,
        height=2,
        command=generate_result
    )

    generate_button.pack(pady=15)

    # PDF BUTTON
    pdf_button = tk.Button(
        window,
        text="Generate PDF Report",
        width=20,
        height=2,
        command=generate_report_pdf
    )

    pdf_button.pack(pady=10)