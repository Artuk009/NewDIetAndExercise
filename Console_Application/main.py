from diet_db.meals import MealsTable, SetMeal, Meals, GetMealID
from diet_db.dates import\
    Dates, InsertDate, DatabaseDate, DatabaseDateID, SetNewDate, SetNewDateID, DatesTable
from diet_db.foods import FoodsTable, FoodCount, Foods, FoodMasterList, GetNutritionInfo
from connection.client_server_connection import ConnectionCredentials, Connection

import json as j

# TODO: Add error handling for invalid input and db check
# TODO: Continue updating tests.
# TODO: Switch to AWS RDS database.


def main():

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

        print()
        print("*" * 39)
        print("* Working with entries for", current_date.date, "*")
        print("*" * 39)
        print()

        choice = input("Select an option: \n"
                       "[1] View Latest Food Entries \n"
                       "[2] View Dates Table \n"
                       "[3] Update the Date \n"
                       "[4] Log a New Food \n"
                       "[5] Add a New Food to the Food Master List \n"
                       "[9] Exit \n")

        dates_table = DatesTable(connection)
        dates_table.get_dates_table()
        meals_table = MealsTable(connection)
        meals_table.get_meals_table(current_date.date_id)
        foods_table = FoodsTable(connection)

        match choice:
            case "1":
                entry_number = input("Enter the number of entries to view: ")
                foods_table.get_foods_table(connection, int(entry_number))
                foods_table.show_foods_table()

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
                    {"fats": fats, "carbs": carbs, "calories": calories, "protein": protein}
                )
                entry = Foods(entry_id, entry_name, entry_nutrition_info)
                entry.add_food_to_food_list_master(connection)

            case "9":
                print("Exiting...")
                exit()

            case _:
                print("Invalid input. Please try again.")
                continue


if __name__ == "__main__":
    main()
