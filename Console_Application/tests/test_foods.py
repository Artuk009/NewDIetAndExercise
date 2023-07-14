import unittest
from diet_db import foods as f


class FoodsTestCase(unittest.TestCase):

    def test_foods_init(self):
        test_food = f.Foods(1, 1, "apple", 1, {"fats": 95, "carbs": 25, "calories": 0.5, "proteins": 0.3})
        assert test_food.id == 1
        assert test_food.meal_id == 1
        assert test_food.food_name == "apple"
        assert test_food.servings == 1
        assert test_food.nutrition_info == {"fats": 95, "carbs": 25, "calories": 0.5, "proteins": 0.3}


if __name__ == '__main__':
    unittest.main()
