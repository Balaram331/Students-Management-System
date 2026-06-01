from database.db import connect_db

from models.marks import Marks


def add_marks(marks: Marks):

    connection = connect_db()

    cursor = connection.cursor()

    query = """
    INSERT INTO marks (
        student_id,
        subject,
        marks
    )

    VALUES (?, ?, ?)
    """

    cursor.execute(
        query,
        (
            marks.student_id,
            marks.subject,
            marks.marks
        )
    )

    connection.commit()

    connection.close()

    print("Marks Added Successfully")