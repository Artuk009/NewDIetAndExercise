import unittest
from unittest.mock import patch
from diet_db import foods as f
import connection.client_server_connection as csc


class FoodsTestCase(unittest.TestCase):

    def test_foods_init(self):
        test_food = f.Foods(1, 1, "apple", 1, {"fats": 95, "carbs": 25, "calories": 0.5, "proteins": 0.3})
        assert test_food.food_id == 1
        assert test_food.meal_id == 1
        assert test_food.food_name == "apple"
        assert test_food.servings == 1
        assert test_food.nutrition_info == {"fats": 95, "carbs": 25, "calories": 0.5, "proteins": 0.3}

    def test_get_latest_food_entry(self):
        pass

    def test_get_food_list_master(self):
        user, password = csc.get_user_and_password()
        connection = csc.get_connection(user, password)
        food_list_master = f.get_food_list_master(connection)
        assert food_list_master[0] == "10 Traditional Wings"

    def test_get_current_foods_count(self):
        user, password = csc.get_user_and_password()
        connection = csc.get_connection(user, password)
        current_foods_count = f.get_current_foods_count(connection)
        assert current_foods_count == 240


if __name__ == '__main__':
    unittest.main()
