import unittest
from connection.client_server_connection import ConnectionCredentials, Connection


class TestConnection(unittest.TestCase):

    def test_ConnectionCredentials(self):

        """Tests that the credentials are correct"""

        credentials = ConnectionCredentials()
        assert credentials.username == 'generic_user'
        assert credentials.password == 'generic_password'

    def test_connection(self):

        """Tests that the connection is established"""

        connection = Connection('generic_user', 'generic_password').get_connection()
        assert connection.is_connected() is True


if __name__ == '__main__':
    unittest.main()
