from database.db import connect_db


def login_user(username, password):
    connection = connect_db()
    cursor = connection.cursor()
    query = """
    SELECT * FROM users 
    WHERE username = ? AND password = ?
    """

    cursor.execute(query, (username, password))
    user =  cursor.fetchone()
    connection.close()
    return user

