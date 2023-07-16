import unittest
from connection import client_server_connection as cdc


class TestConnection(unittest.TestCase):

    def test_user_password(self):
        username, password = cdc.get_user_and_password()
        assert username == 'diet_db_editor'
        assert password == 'diet_db_editor_password'

    def test_connection(self):
        connection = cdc.get_connection('diet_db_editor', 'diet_db_editor_password')
        assert connection.is_connected() is True


if __name__ == '__main__':
    unittest.main()
