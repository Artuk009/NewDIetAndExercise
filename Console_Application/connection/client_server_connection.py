import mysql.connector as conn


def get_user_and_password():

    """Function to get the user and password for the database"""

    username = 'diet_db_editor'
    password = 'diet_db_editor_password'
    return username, password


def get_connection(username, password):

    """Function to create a connection to the database"""

    connection = conn.connect(host="localhost", user=username, password=password, database="diet")
    print("-------------Connected----------------")
    return connection
