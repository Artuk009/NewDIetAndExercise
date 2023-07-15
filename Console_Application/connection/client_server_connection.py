import mysql.connector as conn


def get_user_and_password():
    # Function to get the user's MySQL username and password
    user = 'root'  # input("Enter your MySQL username: ")
    password = 'Artuk150820,./!'  # input("Enter your MySQL password: ")
    return user, password


def get_connection(user, password):
    # Function to create a connection to the database
    connection = conn.connect(host="localhost", user=user, password=password, database="diet")
    print("-------------Connected----------------")
    return connection
