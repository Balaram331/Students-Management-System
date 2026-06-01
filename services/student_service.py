from database.db import connect_db
from models.student import Student



def add_student(student: Student):
    connection=connect_db()
    cursor = connection.cursor()
    query ="""
    INSERT INTO students (name, age, student_class, phone, email)
    VALUES (?, ?, ?, ?,?)
    """
    cursor.execute(query, (
        student.name, 
        student.age, 
        student.student_class, 
        student.phone, 
        student.email))
    connection.commit()
    connection.close()

def get_all_students():
    connection= connect_db()
    cursor = connection.cursor()
    query = "SELECT * FROM students"
    cursor.execute(query)
    students= cursor.fetchall()
    connection.close()
    return students


def delete_student(student_id):
    connection =connect_db()
    cursor = connection.cursor()
    query = "DELETE FROM students WHERE id = ?"
    cursor.execute(query, (student_id,))
    connection.commit()
    connection.close()
    print(f"Student with ID {student_id} has been deleted.")
    

def update_student(phone, email, student_id):

    connection = connect_db()

    cursor = connection.cursor()

    query = """
    UPDATE students
    SET phone = ?, email = ?
    WHERE id = ?
    """

    cursor.execute(query, (phone, email, student_id))

    connection.commit()

    connection.close()

    print("Student Updated Successfully")