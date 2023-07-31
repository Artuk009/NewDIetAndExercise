import mysql.connector as conn


class ConnectionCredentials:

    """Class to get the credentials for the database"""

    sql_username = 'generic_user'
    sql_password = 'generic_password'

    def __init__(self):
        self.username = ConnectionCredentials.sql_username
        self.password = ConnectionCredentials.sql_password

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password


class Connection:

    """Class to create a connection to the database"""

    def __init__(self, username, password):
        self.connection = Connection.connect(self, username, password)

    def get_connection(self):
        return self.connection

    def connect(self, username, password):

        """Function to create a connection to the database"""

        connection = conn.connect(host="localhost", user=username, password=password, database="diet")
        print()
        print("-------------Connected----------------")
        return connection
