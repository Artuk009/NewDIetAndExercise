# Class to create and store food entries in the database
def get_latest_food_entries(connection, limit):
    cursor = connection.cursor(buffered=True)

    # Function to get a limited number of rows from the database
    cursor.callproc("GetFoodsByMealAndDateFromFoods")
    results = next(cursor.stored_results())
    dataset = results.fetchmany(limit)

    # Get columns
    columns = [column[0] for column in results.description]

    # Print the results
    print("Latest 5 entries:")
    print("_" * 88)
    print("| {:>3} | {:>10} | {:>10} | {:>20} | {} | {:>4} | {:>4} | {:>4} | {:>4} |".format(
        'ID', 'Date', 'Meal', 'Food', 'S', 'Carb', 'Fats', 'Prot', 'Cals'
    ))
    print("_" * 88)
    for data in dataset:
        print("| {} | {} | {:>10} | {:>20} | {} | {:>4} | {:>4} | {:>4} | {:>4} |".format(
            data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8]))
    print("_" * 88)

    cursor.close()


class Foods:
    def __init__(self, id, meal_id, food_name, servings, nutrition_info):
        self.id = id
        self.meal_id = meal_id
        self.food_name = food_name
        self.servings = servings
        self.nutrition_info = nutrition_info

    def __str__(self):
        return f"{self.food_name} - {self.nutrition_info}"
