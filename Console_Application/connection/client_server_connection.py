import mysql.connector as conn


def get_user_and_password():

    """Function to get the user and password for the database"""

    user = input("Enter your MySQL username: ")
    password = input("Enter your MySQL password: ")
    return user, password


def get_connection(user, password):

    """Function to create a connection to the database"""

    connection = conn.connect(host="localhost", user=user, password=password, database="diet")
    print("-------------Connected----------------")
    return connection
