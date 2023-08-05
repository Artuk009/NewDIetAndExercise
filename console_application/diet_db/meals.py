class MealsTable:

    """Class to create a meals table object"""

    def __init__(self, connection):
        self.connection = connection
        self.meals_table = []

    def get_meals_table(self, date_id):
        cursor = self.connection.cursor()
        query = "SELECT * FROM meals WHERE date_id = %s"
        cursor.execute(query, (date_id,))
        self.meals_table = cursor.fetchall()
        cursor.close()
        return self.meals_table


class SetMeal:

    """Class to set the meal of the day"""

    def __init__(self):
        pass

    def set_meal(self):

        """Select the meal of the day"""

        meal_of_day = input("Enter the meal of the day: [1]Breakfast [2]Lunch [3]Dinner [4]Post-Workout\n")

        meal = ''
        if meal_of_day == '1':
            meal = 'Breakfast'
        elif meal_of_day == '2':
            meal = 'Lunch'
        elif meal_of_day == '3':
            meal = 'Dinner'
        elif meal_of_day == '4':
            meal = 'Post-Workout'
        else:
            print("Invalid input. Please try again.")
            self.set_meal()
        return meal


class GetMealID:

    """Class to get the meal id"""

    def __init__(self, meal_name, meals_table):
        self.meal_name = meal_name
        self.meals_table = meals_table

    def get_meal_id(self):
        for meal in self.meals_table:
            if meal[2] == self.meal_name:
                return meal[0]
        return None


class Meals:
    def __init__(self, meal_id, date_id, meal_name):
        self.meal_id = meal_id
        self.date_id = date_id
        self.meal_name = meal_name
        self.foods = []

    def __str__(self):
        return f"{self.meal_name}"

    def get_foods_for_meal(self, foods_table):
        pass
