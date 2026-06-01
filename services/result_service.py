from database.db import connect_db


def calculate_result(student_id):

    connection = connect_db()

    cursor = connection.cursor()

    query = """
    SELECT marks
    FROM marks
    WHERE student_id = ?
    """

    cursor.execute(
        query,
        (student_id,)
    )

    marks_data = cursor.fetchall()

    print(marks_data)

    total_marks = 0

    for mark in marks_data:

        total_marks += mark[0]

    subject_count = len(marks_data)

    if subject_count == 0:

        return (
            0,
            0,
            "No Data"
        )

    percentage = (
        total_marks / (subject_count * 100)
    ) * 100

    if percentage >= 90:

        grade = "A+"

    elif percentage >= 80:

        grade = "A"

    elif percentage >= 70:

        grade = "B"

    elif percentage >= 60:

        grade = "C"

    else:

        grade = "Fail"

    connection.close()

    return (
        total_marks,
        percentage,
        grade
    )