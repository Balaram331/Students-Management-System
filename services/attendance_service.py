from database.db import connect_db
from models.attendance import Attendance



def add_attendance(
        attendance: Attendance
):
    connection = connect_db()
    cursor = connection.cursor()

    query = """
    INSERT INTO attendance (
        student_id,
        date,
        status
    ) VALUES (?, ?, ?)"""

    cursor.execute(
        query,
          (
              attendance.student_id,
              attendance.date,
              attendance.status
          )
        )
    
    connection.commit()
    connection.close()
    
    print("Attendance added successfully.")