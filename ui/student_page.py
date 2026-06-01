import tkinter as tk
from tkinter import messagebox, ttk

from models.student import Student

from services.student_service import (
    add_student,
    get_all_students,
    delete_student,
    update_student
)


def open_student_page():

    # WINDOW
    window = tk.Toplevel()

    window.title("Student Management System")

    window.geometry("800x600")

    selected_student_id = None

    # LABELS
    name_label = tk.Label(window, text="Name")
    name_label.pack()

    name_entry = tk.Entry(window)
    name_entry.pack()

    age_label = tk.Label(window, text="Age")
    age_label.pack()

    age_entry = tk.Entry(window)
    age_entry.pack()

    class_label = tk.Label(window, text="Class")
    class_label.pack()

    class_entry = tk.Entry(window)
    class_entry.pack()

    phone_label = tk.Label(window, text="Phone")
    phone_label.pack()

    phone_entry = tk.Entry(window)
    phone_entry.pack()

    email_label = tk.Label(window, text="Email")
    email_label.pack()

    email_entry = tk.Entry(window)
    email_entry.pack()

    # TABLE
    student_table = ttk.Treeview(
        window,
        columns=("ID", "Name", "Age", "Class", "Phone", "Email"),
        show="headings"
    )

    student_table.heading("ID", text="ID")
    student_table.heading("Name", text="Name")
    student_table.heading("Age", text="Age")
    student_table.heading("Class", text="Class")
    student_table.heading("Phone", text="Phone")
    student_table.heading("Email", text="Email")

    student_table.column("ID", width=50)
    student_table.column("Name", width=120)
    student_table.column("Age", width=70)
    student_table.column("Class", width=70)
    student_table.column("Phone", width=120)
    student_table.column("Email", width=200)

    student_table.pack(pady=20)

    # LOAD STUDENTS
    def load_students():

        for row in student_table.get_children():
            student_table.delete(row)

        students = get_all_students()

        for student in students:
            student_table.insert("", tk.END, values=student)

    # CLEAR INPUTS
    def clear_fields():

        name_entry.delete(0, tk.END)
        age_entry.delete(0, tk.END)
        class_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)

    # SELECT STUDENT
    def select_student(event):

        nonlocal selected_student_id

        selected_item = student_table.selection()

        if not selected_item:
            return

        student_data = student_table.item(selected_item)

        values = student_data["values"]

        selected_student_id = values[0]

        clear_fields()

        name_entry.insert(0, values[1])
        age_entry.insert(0, values[2])
        class_entry.insert(0, values[3])
        phone_entry.insert(0, values[4])
        email_entry.insert(0, values[5])

    # SAVE STUDENT
    def save_student():

        name = name_entry.get()
        age = age_entry.get()
        student_class = class_entry.get()
        phone = phone_entry.get()
        email = email_entry.get()

        student = Student(
            name,
            age,
            student_class,
            phone,
            email
        )

        add_student(student)

        load_students()

        clear_fields()

        messagebox.showinfo(
            "Success",
            "Student Added Successfully"
        )

    # DELETE STUDENT
    def remove_student():

        selected_item = student_table.selection()

        if not selected_item:

            messagebox.showwarning(
                "Warning",
                "Please select a student"
            )

            return

        student_data = student_table.item(selected_item)

        student_id = student_data["values"][0]

        delete_student(student_id)

        load_students()

        clear_fields()

        messagebox.showinfo(
            "Success",
            "Student Deleted Successfully"
        )

    # UPDATE STUDENT
    def edit_student():

        nonlocal selected_student_id

        if selected_student_id is None:

            messagebox.showwarning(
                "Warning",
                "Please select a student"
            )

            return

        phone = phone_entry.get()
        email = email_entry.get()

        update_student(
            phone,
            email,
            selected_student_id
        )

        load_students()

        messagebox.showinfo(
            "Success",
            "Student Updated Successfully"
        )

    # BUTTONS
    save_button = tk.Button(
        window,
        text="Add Student",
        command=save_student
    )

    save_button.pack(pady=5)

    delete_button = tk.Button(
        window,
        text="Delete Student",
        command=remove_student,
        bg="red",
        fg="white"
    )

    delete_button.pack(pady=5)

    update_button = tk.Button(
        window,
        text="Update Student",
        command=edit_student,
        bg="blue",
        fg="white"
    )

    update_button.pack(pady=5)

    # TABLE SELECT EVENT
    student_table.bind(
        "<<TreeviewSelect>>",
        select_student
    )

    # LOAD DATA
    load_students()