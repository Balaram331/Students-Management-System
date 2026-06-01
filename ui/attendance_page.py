import tkinter as tk

from tkinter import ttk, messagebox

from datetime import date

from models.attendance import Attendance

from services.attendance_service import add_attendance

from services.student_service import get_all_students


def open_attendance_page():

    # CREATE WINDOW
    window = tk.Toplevel()

    window.title(
        "Attendance Management System"
    )

    window.geometry("500x400")

    # HEADING
    heading_label = tk.Label(
        window,
        text="Attendance Management",
        font=("Arial", 18, "bold")
    )

    heading_label.pack(pady=20)

    # STUDENT LABEL
    student_label = tk.Label(
        window,
        text="Select Student",
        font=("Arial", 12)
    )

    student_label.pack(pady=5)

    # GET STUDENTS FROM DATABASE
    students = get_all_students()

    print(students)

    # STORE FORMATTED NAMES
    student_names = []

    # LOOP THROUGH STUDENTS
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

    # STATUS LABEL
    status_label = tk.Label(
        window,
        text="Select Attendance Status",
        font=("Arial", 12)
    )

    status_label.pack(pady=5)

    # STATUS DROPDOWN
    status_combobox = ttk.Combobox(
        window,
        values=["Present", "Absent"],
        state="readonly",
        width=35
    )

    status_combobox.pack(pady=10)

    # SAVE FUNCTION
    def save_attendance():

        # GET SELECTED VALUES
        selected_student = (
            student_combobox.get()
        )

        selected_status = (
            status_combobox.get()
        )

        # VALIDATION
        if not selected_student:

            messagebox.showwarning(
                "Warning",
                "Please select a student"
            )

            return

        if not selected_status:

            messagebox.showwarning(
                "Warning",
                "Please select attendance status"
            )

            return

        # EXTRACT STUDENT ID
        student_id = int(
            selected_student.split(" - ")[0]
        )

        # GET TODAY DATE
        today = str(date.today())

        # CREATE ATTENDANCE OBJECT
        attendance = Attendance(
            student_id=student_id,
            date=today,
            status=selected_status
        )

        # SAVE TO DATABASE
        add_attendance(attendance)

        # SUCCESS MESSAGE
        messagebox.showinfo(
            "Success",
            "Attendance Saved Successfully"
        )

        # CLEAR FIELDS
        student_combobox.set("")

        status_combobox.set("")

    # SAVE BUTTON
    save_button = tk.Button(
        window,
        text="Save Attendance",
        width=20,
        height=2,
        command=save_attendance
    )

    save_button.pack(pady=20)