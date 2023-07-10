class Diet:
    # Class to create and store food entries in teh database
    class Foods:
        def __init__(self, food_id, meal_id, food_name, servings, nutrition_info):
            self.food_id = food_id
            self.meal_id = meal_id
            self.food_name = food_name
            self.servings = servings
            self.nutrition_info = nutrition_info

        def __str__(self):
            return f"{self.food_name} - {self.nutrition_info}"

    # Class to reference the meals table in the database
    class Meals:
        def __init__(self, meal_id, date_id, meal_name):
            self.meal_id = meal_id
            self.date_id = date_id
            self.meal_name = meal_name

        def __str__(self):
            return f"{self.meal_name}"

    # Class to create and reference the dates in the database
    class Dates:
        def __init__(self, date_id, date):
            self.date_id = date_id
            self.date = date

        def __str__(self):
            return f"{self.date}"

    def get_latest_food_entries(connection, limit):
        cursor = connection.cursor(buffered=True)

        # Function to get a limited number of rows from the database
        cursor.execute(f'''CALL GetFoodsByMealAndDateFromFoods();''')
        records = cursor.fetchmany(limit)
        print("Latest 5 entries:")
        for record in records:
            print(f"[Id: {record[0]}] - {record[1]} - {record[2]} - Name: {record[3]} - Servings: {record[4]} - "
                  f"Fats: {record[5]} - Carbs: {record[6]} - Calories: {record[7]} - Proteins: {record[8]}")

        cursor.close()
