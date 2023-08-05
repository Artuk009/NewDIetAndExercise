import unittest
from connection.client_server_connection import ConnectionCredentials, Connection


class TestConnection(unittest.TestCase):

    def test_ConnectionCredentials(self):

        """Tests that the credentials are correct"""

        credentials = ConnectionCredentials()
        assert credentials.username == 'diet_user'
        assert credentials.password == 'diet_user'


if __name__ == '__main__':
    unittest.main()
