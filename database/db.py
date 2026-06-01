import sqlite3
DATABASE_NAME = "database/school.db"


def connect_db():
    connection=sqlite3.connect(DATABASE_NAME)
    return connection

def execute_query(query, parameters=()):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute(query, parameters)
    connection.commit()
    connection.close()
    


