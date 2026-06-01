from database.db import execute_query

def create_students_table():
    query = """
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        student_class TEXT ,
        phone TEXT ,
        email TEXT 
        
    )
    """
    execute_query(query)


def create_users_table():
    query = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT, 
        role TEXT
    )
    """
    execute_query(query)


def create_attendance_table():
    query = """
    CREATE TABLE IF NOT EXISTS attendance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        date TEXT,
        status TEXT
    )
    """
    execute_query(query)

def create_marks_table():

    query = """
    CREATE TABLE IF NOT EXISTS marks (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        student_id INTEGER,

        subject TEXT,

        marks INTEGER
    )
    """

    execute_query(query)



def create_results_table():
    query = """
    CREATE TABLE IF NOT EXISTS results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        subject TEXT,
        marks REAL,
        grade TEXT
    )
    """
    execute_query(query)

def create_all_tables():
    create_students_table()
    create_users_table()
    create_attendance_table()
    create_results_table()
    create_marks_table()
