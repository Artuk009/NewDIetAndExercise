class Diet:
    # Class to create and store food entries in teh database
    class Foods:
        def __init__(self, id, meal_id, food_name, servings, nutrition_info):
            self.id = id
            self.meal_id = meal_id
            self.food_name = food_name
            self.servings = servings
            self.nutrition_info = nutrition_info

        def __str__(self):
            return f"{self.food_name} - {self.nutrition_info}"

    # Class to reference the meals table in the database
    class Meals:
        def __init__(self, id, date_id, meal_name):
            self.id = id
            self.date_id = date_id
            self.meal_name = meal_name

        def __str__(self):
            return f"{self.meal_name}"

    def get_latest_food_entries(self, connection, limit):
        cursor = connection.cursor(buffered=True)

        # Function to get a limited number of rows from the database
        cursor.callproc("GetFoodsByMealAndDateFromFoods")
        results = next(cursor.stored_results())
        dataset = results.fetchmany(limit)

        # Get columns
        columns = [column[0] for column in results.description]

        # Print the results
        print("Latest 5 entries:")
        print(columns)
        for data in dataset:
            print(f"{data[0]} - {data[1]} - {data[2]} - {data[3]} - {data[4]} -"
                  f" {data[5]} - {data[6]} - {data[7]} - {data[8]}")

        cursor.close()
