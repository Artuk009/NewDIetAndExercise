from diet_db.meals import MealsTable, SetMeal, GetMealID
from diet_db.dates import \
    Dates, InsertDate, DatabaseDate, DatabaseDateID, SetNewDate, SetNewDateID, DatesTable
from diet_db.foods import FoodsTable, FoodCount, Foods, FoodMasterList, GetNutritionInfo
from diet_db.body_measurements import BodyMeasurementsTable, MeasurementCount, BodyMeasurements
from connection.client_server_connection import ConnectionCredentials, Connection
from interface.printer import Printer
from interface.selections import Selections

import json as j


class Application:
    def run(self):

        # Get credentials for database
        credentials = ConnectionCredentials()
        host = input("Input AWS RDS host: ")

        # Chose an option to execute
        while True:

            # Get connection to the database
            connection = Connection(
                host,
                credentials.get_username(),
                credentials.get_password(),
            ).get_connection()

            # Get the latest date and date id
            current_date = Dates(
                DatabaseDateID(connection).get_latest_date_id(),
                DatabaseDate(connection).get_latest_date()
            )

            printer = Printer()
            selection = Selections()
            printer.print_date_heading(current_date.date)
            choice = printer.print_options()

            dates_table = DatesTable(connection)
            dates_table.get_dates_table()
            meals_table = MealsTable(connection)
            meals_table.get_meals_table(current_date.date_id)
            foods_table = FoodsTable(connection)
            body_measurements_table = BodyMeasurementsTable(connection)

            match choice:
                case "1":
                    selection.show_ftable(foods_table)

                case "2":
                    dates_table.show_dates_table()

                case "3":
                    day = input("Enter the day of the month: ")
                    new_id = SetNewDateID(dates_table.dates_table).set_new_date_id()
                    new_date = SetNewDate(day).set_new_date()
                    print("The date has been set to", new_date, "with an id of", new_id)

                    date_entry = Dates(new_id, new_date)
                    InsertDate(date_entry.date_id, date_entry.date).add_date_to_db(connection)

                case "4":
                    entry_id = FoodCount(connection).get_food_count() + 1
                    meal = SetMeal().set_meal()
                    entry_meal_id = GetMealID(meal, meals_table.meals_table).get_meal_id()
                    entry_name = input("What food would you like to add? ")

                    # Check if food is in master list
                    food_master_list = FoodMasterList(connection)
                    food_master_list.get_food_master_list()
                    if entry_name not in food_master_list.get_names():
                        print("That food is not in the master list. Please add it to the master list.")
                        continue

                    entry_servings = input("How many servings? ")
                    entry_nutrition_info = GetNutritionInfo(entry_name, connection).get_nutrition_info()
                    entry = Foods(entry_id, entry_meal_id, entry_name, entry_servings, entry_nutrition_info)
                    entry.add_food(connection)

                case "5":
                    entry_id = FoodCount(connection).get_food_list_master_count() + 1
                    entry_name = input("What food would you like to add to teh master list? ")
                    fats = int(input("How many g of fats? "))
                    carbs = int(input("How many g of carbs? "))
                    calories = int(input("How many calories? "))
                    protein = int(input("How many g of protein? "))

                    entry_nutrition_info = j.dumps(
                        {"fats": fats, "carbs": carbs, "calories": calories, "proteins": protein}
                    )

                    entry = Foods(entry_id, entry_name, entry_nutrition_info)
                    entry.add_food_to_food_list_master(connection)

                case "6":
                    selection.show_bmtable(body_measurements_table)

                case "7":
                    entry_id = MeasurementCount(connection).get_measurement_count() + 1
                    date_id = current_date.date_id
                    bf_percentage = float(input("What is your body fat percentage? "))
                    fat_mass = float(input("What is your fat mass? "))
                    body_weight = float(input("What is your body weight? "))
                    muscle_mass = float(input("What is your muscle mass? "))

                    # Determine workout type.
                    type_choice = input("Enter Workout Type: [1] CHST, [2] BACK, [3] SHDR, [4] LEGS, [5] REST")
                    if type_choice == '1':
                        workout_type = 'CHST'
                    elif type_choice == '2':
                        workout_type = 'BACK'
                    elif type_choice == '3':
                        workout_type = 'SHDR'
                    elif type_choice == '4':
                        workout_type = 'LEGS'
                    elif type_choice == '5':
                        workout_type = 'REST'
                    else:
                        print("Invalid Choice")
                        raise Exception("Invalid Choice")

                    measurements = j.dumps(
                        {"body_fat": bf_percentage, "fat_mass": fat_mass, "body_weight": body_weight,
                         "muscle_mass": muscle_mass, "workout_type": workout_type}
                    )

                    entry = BodyMeasurements(connection, entry_id, date_id, measurements)
                    entry.add_measurements()

                case "9":
                    print("Exiting...")
                    exit()

                case _:
                    print("Invalid input. Please try again.")
                    continue
