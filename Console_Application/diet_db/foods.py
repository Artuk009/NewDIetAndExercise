def get_latest_food_entries(connection, limit):

    """Function to get the latest food entries from the database and print them to the console"""

    cursor = connection.cursor(buffered=True)
    cursor.callproc("GetFoodsByMealAndDateFromFoods")
    results = next(cursor.stored_results())
    dataset = results.fetchmany(limit)
    # Print the results
    print("Latest 5 entries:")
    print("_" * 93)
    print("| {:<3} | {:<10} | {:<15} | {:<20} | {} | {:<4} | {:<4} | {:<4} | {:<4} |".format(
        'ID', 'Date', 'Meal', 'Food', 'S', 'Carb', 'Fats', 'Prot', 'Cals'
    ))
    print("_" * 93)
    for data in dataset:
        print("| {} | {} | {:<15} | {:<20} | {} | {:<4} | {:<4} | {:<4} | {:<4} |".format(
            data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8]))
    print("_" * 93)

    cursor.close()


def get_food_list_master(connection):
    cursor = connection.cursor(buffered=True)

    """Function to get all foods from the food_list_master table and store the names in a list"""

    existing_foods = []
    query = "SELECT food_name FROM food_list_master_json"
    cursor.execute(query)
    for food in cursor:
        existing_foods.append(food[0])
    cursor.close()
    return existing_foods


def get_current_foods_count(connection):

    """Function to get the current foods from the database"""

    cursor = connection.cursor(buffered=True)
    cursor.execute("SELECT * FROM foods_json")
    current_foods = cursor.fetchall()
    cursor.close()
    return len(current_foods)


class Foods:

    """Class to create and store food entries in the database"""

    def __init__(self, food_id, meal_id, food_name, servings, nutrition_info):
        self.food_id = food_id
        self.meal_id = meal_id
        self.food_name = food_name
        self.servings = servings
        self.nutrition_info = nutrition_info

    def __str__(self):
        return f"{self.food_name} - {self.nutrition_info}"
