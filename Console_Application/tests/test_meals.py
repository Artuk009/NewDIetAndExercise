import unittest
from diet_db import meals


class MealsTestCase(unittest.TestCase):

    def test_meals_init(self):
        test_meal = meals.Meals(1, 1, "Breakfast")
        assert test_meal.id == 1
        assert test_meal.date_id == 1
        assert test_meal.meal_name == "Breakfast"


if __name__ == '__main__':
    unittest.main()
