import tkinter as tk

from ui.student_page import open_student_page

from ui.attendance_page import open_attendance_page

from ui.marks_page import open_marks_page

from ui.result_page import open_result_page

from ui.analytics_page import open_analytics_page


def open_dashboard():

    dashboard = tk.Tk()

    dashboard.title(
        "Student Management Dashboard"
    )

    dashboard.geometry("800x600")

    heading_label = tk.Label(
        dashboard,
        text="Welcome to the Student Management Dashboard",
        font=("Arial", 20)
    )

    heading_label.pack(pady=20)

    # STUDENT BUTTON
    student_button = tk.Button(
        dashboard,
        text="Manage Students",
        width=25,
        height=2,
        command=open_student_page
    )

    student_button.pack(pady=10)

    # ATTENDANCE BUTTON
    attendance_button = tk.Button(
        dashboard,
        text="Manage Attendance",
        width=25,
        height=2,
        command=open_attendance_page
    )

    attendance_button.pack(pady=10)

    # MARKS BUTTON
    marks_button = tk.Button(
        dashboard,
        text="Manage Marks",
        width=25,
        height=2,
        command=open_marks_page
    )

    marks_button.pack(pady=10)

    # RESULTS BUTTON
    results_button = tk.Button(
        dashboard,
        text="Manage Results",
        width=25,
        height=2,
        command=open_result_page
    )

    results_button.pack(pady=10)

    # ANALYTICS BUTTON
    analytics_button = tk.Button(
        dashboard,
        text="Analytics Dashboard",
        width=25,
        height=2,
        command=open_analytics_page
    )

    analytics_button.pack(pady=10)

    dashboard.mainloop()