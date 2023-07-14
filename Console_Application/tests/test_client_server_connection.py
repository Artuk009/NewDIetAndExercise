import unittest
from connection import client_server_connection as cdc


class TestConnection(unittest.TestCase):

    def test_user_password(self):
        cdc.input = lambda _: "test_client"
        user, password = cdc.get_user_and_password()
        assert user == "test_client"
        assert password == "test_client"

    def test_connection(self):
        connection = cdc.get_connection("test_user", "test_pass")
        assert connection.is_connected() is True


if __name__ == '__main__':
    unittest.main()
