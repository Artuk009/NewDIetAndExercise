import unittest
from connection.client_server_connection import ConnectionCredentials, Connection


class TestConnection(unittest.TestCase):

    def test_ConnectionCredentials(self):

        """Tests that the credentials are correct"""

        credentials = ConnectionCredentials()
        assert credentials.username == 'diet_db_editor'
        assert credentials.password == 'diet_db_editor_password'

    def test_connection(self):

        """Tests that the connection is established"""

        connection = Connection('diet_db_editor', 'diet_db_editor_password').get_connection()
        assert connection.is_connected() is True


if __name__ == '__main__':
    unittest.main()
