def get_meals_table(connection, date_id):
    cursor = connection.cursor()
    query = "SELECT * FROM meals WHERE date_id = %s"
    cursor.execute(query, (date_id,))
    meals_table = cursor.fetchall()
    cursor.close()
    return meals_table


def set_meal():

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
        set_meal()
    return meal


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
