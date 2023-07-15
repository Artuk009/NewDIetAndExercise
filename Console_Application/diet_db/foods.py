# Class to create and store food entries in the database
def get_latest_food_entries(connection, limit):
    cursor = connection.cursor(buffered=True)

    # Function to get a limited number of rows from the database
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

    # Function to get all foods from the food_list_master table and store the names in a list
    existing_foods = []
    query = "SELECT food_name FROM food_list_master_json"
    cursor.execute(query)
    for food in cursor:
        existing_foods.append(food[0])

    cursor.close()
    return existing_foods


def set_meal():
    # Select the meal of the day
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


def get_current_foods_count(connection):
    cursor = connection.cursor(buffered=True)

    # Function to get the current foods from the database
    cursor.execute("SELECT * FROM foods_json")
    current_foods = cursor.fetchall()

    cursor.close()
    return len(current_foods)


class Foods:
    def __init__(self, id, meal_id, food_name, servings, nutrition_info):
        self.id = id
        self.meal_id = meal_id
        self.food_name = food_name
        self.servings = servings
        self.nutrition_info = nutrition_info

    def __str__(self):
        return f"{self.food_name} - {self.nutrition_info}"
