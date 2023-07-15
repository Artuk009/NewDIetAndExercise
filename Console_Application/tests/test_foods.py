import unittest
from diet_db import foods as f
import connection.client_server_connection as csc
from unittest.mock import patch


class FoodsTestCase(unittest.TestCase):

    def test_foods_init(self):
        test_food = f.Foods(1, 1, "apple", 1, {"fats": 95, "carbs": 25, "calories": 0.5, "proteins": 0.3})
        assert test_food.id == 1
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

    @patch('builtins.input', return_value="1")
    def test_set_breakfast(self, mock_input):
        self.assertEqual(f.set_meal(), "Breakfast")

    @patch('builtins.input', return_value="2")
    def test_set_luch(self, mock_input):
        self.assertEqual(f.set_meal(), "Lunch")

    @patch('builtins.input', return_value="3")
    def test_set_dinner(self, mock_input):
        self.assertEqual(f.set_meal(), "Dinner")

    @patch('builtins.input', return_value="4")
    def test_set_snack(self, mock_input):
        self.assertEqual(f.set_meal(), "Post-Workout")

    def test_get_current_foods_count(self):
        user, password = csc.get_user_and_password()
        connection = csc.get_connection(user, password)
        current_foods_count = f.get_current_foods_count(connection)
        assert current_foods_count == 231


if __name__ == '__main__':
    unittest.main()
