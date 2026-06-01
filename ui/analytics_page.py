import tkinter as tk

import matplotlib.pyplot as plt

from services.analytics_service import (
    get_analytics_data
)


def open_analytics_page():

    # CREATE WINDOW
    window = tk.Toplevel()

    window.title(
        "Analytics Dashboard"
    )

    window.geometry("600x600")

    # GET ANALYTICS DATA
    analytics = (
        get_analytics_data()
    )

    # HEADING
    title_label = tk.Label(
        window,
        text="Analytics Dashboard",
        font=("Arial", 18, "bold")
    )

    title_label.pack(pady=20)

    # TOTAL STUDENTS
    total_label = tk.Label(
        window,
        text=f"Total Students: {analytics.total_students}",
        font=("Arial", 14)
    )

    total_label.pack(pady=10)

    # AVERAGE MARKS
    average_label = tk.Label(
        window,
        text=f"Average Marks: {analytics.average_marks:.2f}",
        font=("Arial", 14)
    )

    average_label.pack(pady=10)

    # HIGHEST MARKS
    highest_label = tk.Label(
        window,
        text=f"Highest Marks: {analytics.highest_marks}",
        font=("Arial", 14)
    )

    highest_label.pack(pady=10)

    # PIE CHART FUNCTION
    def show_pie_chart():

        plt.figure(figsize=(6, 5))

        labels = [
            "Pass",
            "Fail"
        ]

        sizes = [
            80,
            20
        ]

        plt.pie(
            sizes,
            labels=labels,
            autopct="%1.1f%%"
        )

        plt.title(
            "Pass vs Fail Students"
        )

        plt.tight_layout()

        plt.show()

    # PIE CHART BUTTON
    pie_button = tk.Button(
        window,
        text="Show Pie Chart",
        width=20,
        height=2,
        command=show_pie_chart
    )

    pie_button.pack(pady=10)

    # BAR GRAPH FUNCTION
    def show_bar_graph():

        plt.figure(figsize=(6, 5))

        subjects = [
            "Math",
            "Physics",
            "English"
        ]

        marks = [
            90,
            80,
            70
        ]

        plt.bar(
            subjects,
            marks
        )

        plt.xlabel("Subjects")

        plt.ylabel("Marks")

        plt.title(
            "Subject-wise Marks"
        )

        plt.tight_layout()

        plt.show()

    # BAR GRAPH BUTTON
    bar_button = tk.Button(
        window,
        text="Show Bar Graph",
        width=20,
        height=2,
        command=show_bar_graph
    )

    bar_button.pack(pady=10)