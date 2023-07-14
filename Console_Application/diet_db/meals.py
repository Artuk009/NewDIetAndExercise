# Class to reference the meals table in the database
class Meals:
    def __init__(self, id, date_id, meal_name):
        self.id = id
        self.date_id = date_id
        self.meal_name = meal_name

    def __str__(self):
        return f"{self.meal_name}"
