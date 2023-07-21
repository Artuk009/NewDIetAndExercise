import pytest
import unittest
from unittest.mock import patch
from diet_db.foods import FoodsTable, FoodCount, Foods, FoodMasterList
from connection.client_server_connection import ConnectionCredentials, Connection


class FoodsTestCase(unittest.TestCase):

    # Get connection to the database
    pytest.credentials = ConnectionCredentials()
    pytest.connection = Connection(
        pytest.credentials.get_username(),
        pytest.credentials.get_password()
    ).get_connection()

    # Initialize the foods table with large number of entries for count test.
    pytest.foods_table = FoodsTable(pytest.connection)
    pytest.foods_table.get_foods_table(pytest.connection, 999999999)

    def test_get_foods_table(self):

        """Tests that the first entry in the table matches the database"""

        cursor = pytest.connection.cursor()
        query = """
        SELECT f.id, d.date, m.meal, f.food_name, f.servings, f.nutrition_info->'$.carbs' AS carbs, 
        f.nutrition_info->'$.fats' AS fats, f.nutrition_info->'$.proteins' AS proteins,
        f.nutrition_info->'$.calories' AS calories
        FROM meals m
        INNER JOIN foods_json f on f.meal_id = m.id
        INNER JOIN dates_2023 d on d.id = m.date_id
        ORDER BY f.id DESC LIMIT 1;"""
        cursor.execute(query)
        latest_food = cursor.fetchone()
        cursor.close()
        self.assertEqual(pytest.foods_table.foods_table[0], latest_food)

    def test_get_food_master_list(self):

        """Tests that the first entry in the food master list matches the database"""

        food_master_list = FoodMasterList(pytest.connection).get_food_master_list()
        assert food_master_list[0][1] == "Oatmeal"

    def test_get_current_foods_count(self):

        """Tests that the current foods count matches the database"""

        current_foods_count = FoodCount(pytest.connection).get_food_count()
        assert current_foods_count == len(pytest.foods_table.foods_table)


if __name__ == '__main__':
    unittest.main()
