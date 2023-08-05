import mysql.connector as conn


class ConnectionCredentials:

    """Class to get the credentials for the database"""

    sql_username = 'diet_user'
    sql_password = 'diet_user'

    def __init__(self):
        self.username = ConnectionCredentials.sql_username
        self.password = ConnectionCredentials.sql_password

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password


class Connection:

    """Class to create a connection to the database"""

    def __init__(self, host, username, password):
        self.connection = Connection.connect(self, host, username, password)

    def get_connection(self):
        return self.connection

    def connect(self, host, username, password):

        """Function to create a connection to the database"""

        connection = conn.connect(host=host, user=username, password=password, database="diet")
        print()
        print("-------------Connected----------------")
        return connection
