import unittest
import diet


class DatesTestCase(unittest.TestCase):

    def test_foods_init(self):
        test_food = diet.Diet.Foods(1, 1, "apple", 1, {"fats": 95, "carbs": 25, "calories": 0.5, "proteins": 0.3})
        assert test_food.id == 1
        assert test_food.meal_id == 1
        assert test_food.food_name == "apple"
        assert test_food.servings == 1
        assert test_food.nutrition_info == {"fats": 95, "carbs": 25, "calories": 0.5, "proteins": 0.3}

    def test_meals_init(self):
        test_meal = diet.Diet.Meals(1, 1, "Breakfast")
        assert test_meal.id == 1
        assert test_meal.date_id == 1
        assert test_meal.meal_name == "Breakfast"


if __name__ == '__main__':
    unittest.main()






