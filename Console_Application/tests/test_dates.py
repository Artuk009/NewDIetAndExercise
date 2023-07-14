import unittest
from diet_db import dates as d
import connection.client_server_connection as csc
import datetime


class DatesTestCase(unittest.TestCase):

    def test_dates_init(self):
        test_date = d.Dates(1, "2021-04-01")
        assert test_date.date_id == 1
        assert test_date.date == "2021-04-01"

    def test_get_dates(self):
        user, password = csc.get_user_and_password()
        connection = csc.get_connection(user, password)
        dates_table = d.get_dates(connection)
        assert dates_table[0] == (21,  datetime.date(2023, 7, 13))

    # TODO: Finish these tests
    def test_set_date(self):
        pass

    def test_add_date_to_db(self):
        pass


if __name__ == '__main__':
    unittest.main()
