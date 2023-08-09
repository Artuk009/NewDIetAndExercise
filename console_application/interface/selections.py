from diet_db.body_measurements import BodyMeasurementsTable, MeasurementCount, BodyMeasurements
from diet_db.dates import DatesTable, Dates, DatabaseDateID, DatabaseDate, SetNewDateID, SetNewDate, InsertDate
from diet_db.foods import FoodsTable, FoodCount, FoodMasterList, GetNutritionInfo, Foods
from diet_db.meals import MealsTable, SetMeal, GetMealID

import json as j


class Selections:

    def __init__(self, connection):
        self.connection = connection
        self.current_date = Dates(
                DatabaseDateID(connection).get_latest_date_id(),
                DatabaseDate(connection).get_latest_date()
            )
        self.dates_table = DatesTable(connection)
        self.dates_table.get_dates_table()
        self.meals_table = MealsTable(connection)
        self.meals_table.get_meals_table(self.current_date.date_id)
        self.foods_table = FoodsTable(connection)
        self.body_measurements_table = BodyMeasurementsTable(connection)

    def show_ftable(self):
        entry_number = input("Enter the number of entries to view: ")
        self.foods_table.get_foods_table(int(entry_number))
        self.foods_table.show_foods_table()

    def show_bmtable(self):
        entry_number = input("Enter the number of entries to view: ")
        self.body_measurements_table.get_body_measurements_table(int(entry_number))
        self.body_measurements_table.show_body_measurements_table()

    def show_dtable(self):
        self.dates_table.show_dates_table()

    def insert_date(self):
        # TODO: Manual execution test check
        day = input("Enter the day of the month: ")
        new_id = SetNewDateID(self.dates_table.dates_table).set_new_date_id()
        new_date = SetNewDate(day).set_new_date()
        print("The date has been set to", new_date, "with an id of", new_id)

        date_entry = Dates(new_id, new_date)
        InsertDate(date_entry.date_id, date_entry.date).add_date_to_db(self.connection)

    def insert_food(self):
        entry_id = FoodCount(self.connection).get_food_count() + 1
        meal = SetMeal().set_meal()
        entry_meal_id = GetMealID(meal, self.meals_table.meals_table).get_meal_id()
        entry_name = input("What food would you like to add? ")

        # Check if food is in master list
        food_master_list = FoodMasterList(self.connection)
        food_master_list.get_food_master_list()
        if entry_name not in food_master_list.get_names():
            print("That food is not in the master list. Please add it to the master list.")
            return

        entry_servings = input("How many servings? ")
        entry_nutrition_info = GetNutritionInfo(entry_name, self.connection).get_nutrition_info()
        entry = Foods(entry_id, entry_meal_id, entry_name, entry_servings, entry_nutrition_info)
        entry.add_food(self.connection)

    def insert_flmaster(self):
        # TODO: Manual execution test check
        entry_id = FoodCount(self.connection).get_food_list_master_count() + 1
        entry_name = input("What food would you like to add to the master list? ")
        fats = int(input("How many g of fats? "))
        carbs = int(input("How many g of carbs? "))
        calories = int(input("How many calories? "))
        protein = int(input("How many g of protein? "))

        entry_nutrition_info = j.dumps(
            {"fats": fats, "carbs": carbs, "calories": calories, "proteins": protein}
        )

        entry = Foods(entry_id, entry_name, entry_nutrition_info)
        entry.add_food_to_food_list_master(self.connection)

    def insert_bmeasurements(self):
        # TODO: Manual execution test check
        entry_id = MeasurementCount(self.connection).get_measurement_count() + 1
        date_id = self.current_date.date_id
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

        entry = BodyMeasurements(self.connection, entry_id, date_id, measurements)
        entry.add_measurements()
