import tkinter as tk

from tkinter import ttk, messagebox

from models.marks import Marks

from services.marks_service import add_marks

from services.student_service import get_all_students


def open_marks_page():

    window = tk.Toplevel()

    window.title(
        "Marks Management"
    )

    window.geometry("500x500")

    # STUDENT LABEL
    student_label = tk.Label(
        window,
        text="Select Student"
    )

    student_label.pack(pady=5)

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
        state="readonly"
    )

    student_combobox.pack(pady=5)

    # SUBJECT LABEL
    subject_label = tk.Label(
        window,
        text="Enter Subject"
    )

    subject_label.pack(pady=5)

    # SUBJECT ENTRY
    subject_entry = tk.Entry(window)

    subject_entry.pack(pady=5)

    # MARKS LABEL
    marks_label = tk.Label(
        window,
        text="Enter Marks"
    )

    marks_label.pack(pady=5)

    # MARKS ENTRY
    marks_entry = tk.Entry(window)

    marks_entry.pack(pady=5)

    # SAVE FUNCTION
    def save_marks():

        student_value = (
            student_combobox.get()
        )

        subject = (
            subject_entry.get()
        )

        marks_value = (
            marks_entry.get()
        )

        # EMPTY VALIDATION
        if not student_value or not subject or not marks_value:

            messagebox.showwarning(
                "Warning",
                "Please fill all fields"
            )

            return

        # MARKS VALIDATION
        if not marks_value.isdigit():

            messagebox.showerror(
                "Error",
                "Marks must be numeric"
            )

            return

        # CONVERT TO INTEGER
        marks_value = int(marks_value)

        # RANGE VALIDATION
        if marks_value < 0 or marks_value > 100:

            messagebox.showerror(
                "Error",
                "Marks must be between 0 and 100"
            )

            return

        # EXTRACT STUDENT ID
        student_id = (
            student_value.split(" - ")[0]
        )

        # CREATE OBJECT
        marks = Marks(
            student_id,
            subject,
            marks_value
        )

        # SAVE TO DATABASE
        add_marks(marks)

        # SUCCESS MESSAGE
        messagebox.showinfo(
            "Success",
            "Marks Added Successfully"
        )

        # CLEAR FIELDS
        subject_entry.delete(0, tk.END)

        marks_entry.delete(0, tk.END)

    # SAVE BUTTON
    save_button = tk.Button(
        window,
        text="Save Marks",
        command=save_marks
    )

    save_button.pack(pady=20)