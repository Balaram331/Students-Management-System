from database.db import connect_db
from models.analytics import Analytics

def get_analytics_data():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM students"
    )
    total_students= (
        cursor.fetchone()[0]
    )

    cursor.execute(
        "SELECT AVG(marks) FROM marks"
    )
    average_marks = (
        cursor.fetchone()[0]
    )

    cursor.execute(
        "SELECT MAX(marks) FROM marks"
    )
    highest_marks = (
        cursor.fetchone()[0]
    )

    return Analytics(
        total_students=total_students,
        average_marks=average_marks,
        highest_marks=highest_marks
    )


