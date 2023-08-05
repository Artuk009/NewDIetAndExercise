import datetime
import pytest
import unittest
from unittest.mock import patch
from diet_db.dates import \
    DatesTable, SetNewDate, SetNewDateID, DatabaseDateID, DatabaseDate, Dates, InsertDate
from connection.client_server_connection import ConnectionCredentials, Connection


class DatesTestCases(unittest.TestCase):

    # Get connection to the database
    pytest.credentials = ConnectionCredentials()
    pytest.connection = Connection(
        pytest.credentials.get_username(),
        pytest.credentials.get_password()
    ).get_connection()

    # Initialize the dates table
    pytest.dates_table = DatesTable(pytest.connection)
    pytest.dates_table.get_dates_table()

    # Initialize the day for testing the new date
    pytest.day = '01'

    def test_get_dates_table(self):

        """Tests that the first entry in the table matches the database"""

        cursor = pytest.connection.cursor()
        query = "SELECT * FROM dates_2023 ORDER BY id DESC LIMIT 1"
        cursor.execute(query)
        latest_date = cursor.fetchone()
        cursor.close()
        self.assertEqual(pytest.dates_table.dates_table[0], latest_date)

    @patch('builtins.input', return_value="y")
    def test_set_new_date(self, mock_input):

        """Tests that the new date and passed day match"""

        new_date = SetNewDate(pytest.day).set_new_date()
        year_month = datetime.datetime.now().strftime("%Y-%m")
        assert new_date == f"{year_month}-{pytest.day}"

    def test_set_new_date_id(self):

        """Tests that the new date id is the incremented latest date id in the database"""

        new_id = SetNewDateID(pytest.dates_table.dates_table).set_new_date_id()
        cursor = pytest.connection.cursor()
        query = "SELECT id FROM dates_2023 ORDER BY id DESC LIMIT 1"
        cursor.execute(query)
        latest_date_id = cursor.fetchone()[0]
        cursor.close()
        self.assertEqual(new_id, latest_date_id + 1)

    def test_get_latest_date_id(self):

        """Test the latest date id is correct by comparing it to the dates table"""

        self.assertEqual(
            DatabaseDateID(pytest.connection).get_latest_date_id(),
            pytest.dates_table.dates_table[0][0]
        )

    def test_get_latest_date(self):

        """Test the latest date is correct by comparing it to the dates table"""

        self.assertEqual(
            DatabaseDate(pytest.connection).get_latest_date(),
            pytest.dates_table.dates_table[0][1]
        )

    def test_get_meals_for_date(self):

        """Test that the meals for the latest date are correct"""
        # Need to adjust meals module to apply SOLID principles before this test can be written
        pass

    @patch('builtins.input', return_value="y")
    def test_add_date_to_db(self, mock_input):

        """Test that the new date is added to the database"""

        with unittest.mock.patch.object(
                InsertDate, 'add_date_to_db', return_value=None
        ) as mock_method:
            date_entry = Dates(
                SetNewDateID(pytest.dates_table.dates_table).set_new_date_id(),
                SetNewDate(pytest.day).set_new_date()
            )
            InsertDate(date_entry.date_id, date_entry.date).add_date_to_db(pytest.connection)
            mock_method.assert_called_once_with(pytest.connection)


if __name__ == '__main__':
    unittest.main()
