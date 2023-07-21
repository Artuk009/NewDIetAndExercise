import pytest
import unittest
from unittest.mock import patch
from connection.client_server_connection import ConnectionCredentials, Connection
from diet_db.meals import MealsTable, SetMeal, Meals
from diet_db.dates import DatabaseDateID


class MyTestCase(unittest.TestCase):

    # Get connection to the database
    pytest.credentials = ConnectionCredentials()
    pytest.connection = Connection(
        pytest.credentials.get_username(),
        pytest.credentials.get_password()
    ).get_connection()

    # Get the latest date id for testing
    pytest.latest_date_id = DatabaseDateID(pytest.connection).get_latest_date_id()

    # Initialize the meals table
    pytest.meals_table = MealsTable(pytest.connection)
    pytest.meals_table.get_meals_table(pytest.latest_date_id)

    # Initialize the meal
    pytest.meal = SetMeal()

    def test_get_meals_table(self):

        """Tests that the first entry in the table matches the database"""

        cursor = pytest.connection.cursor()
        query = "SELECT * FROM meals ORDER BY id DESC LIMIT 1"
        cursor.execute(query)
        latest_meal = cursor.fetchone()
        cursor.close()
        self.assertEqual(pytest.meals_table.meals_table[3], latest_meal)

    @patch('builtins.input', return_value="1")
    def test_set_breakfast(self, mock_input):

        """Tests that the meal is set to breakfast"""

        self.assertEqual(pytest.meal.set_meal(), "Breakfast")

    @patch('builtins.input', return_value="2")
    def test_set_lunch(self, mock_input):

        """Tests that the meal is set to lunch"""

        self.assertEqual(pytest.meal.set_meal(), "Lunch")

    @patch('builtins.input', return_value="3")
    def test_set_dinner(self, mock_input):

        """Tests that the meal is set to dinner"""

        self.assertEqual(pytest.meal.set_meal(), "Dinner")

    @patch('builtins.input', return_value="4")
    def test_set_snack(self, mock_input):

        """Tests that the meal is set to snack"""

        self.assertEqual(pytest.meal.set_meal(), "Post-Workout")


if __name__ == '__main__':
    unittest.main()
