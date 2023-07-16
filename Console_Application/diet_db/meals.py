def get_meals(connection, date_id):
    cursor = connection.cursor()
    query = "SELECT * FROM meals WHERE date_id = %s"
    cursor.execute(query, (date_id,))
    meals_table = cursor.fetchall()
    cursor.close()
    return meals_table


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