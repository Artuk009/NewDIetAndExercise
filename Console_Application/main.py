from diet_db.meals import MealsTable, SetMeal, Meals
from diet_db.dates import\
    Dates, InsertDate, DatabaseDate, DatabaseDateID, SetNewDate, SetNewDateID, DatesTable
from diet_db.foods import FoodsTable, FoodCount, Foods, FoodMasterList
from connection.client_server_connection import ConnectionCredentials, Connection

# TODO: Implement inserting the new food entries into the database
# TODO: Continue updating tests.


def main():

    # Get credentials for database
    credentials = ConnectionCredentials()

    # Chose an option to execute
    while True:

        # Get connection to the database
        connection = Connection(
            credentials.get_username(),
            credentials.get_password()
        ).get_connection()

        # Get the latest date and date id
        current_date = Dates(
            DatabaseDateID(connection).get_latest_date_id(),
            DatabaseDate(connection).get_latest_date()
        )

        print("*" * 39)
        print("* Working with entries for", current_date.date, "*")
        print("*" * 39)

        choice = input("Select an option: \n"
                       "[1] View Latest Food Entries \n"
                       "[2] View Dates Table \n"
                       "[3] Update the Date \n"
                       "[4] Log a New Food \n"
                       "[9] Exit \n")

        dates_table = DatesTable(connection)
        dates_table.get_dates_table()
        meals_table = MealsTable(connection)
        meals_table.get_meals_table(current_date.date_id)
        foods_table = FoodsTable(connection)
        foods_table.get_foods_table(connection, 5)

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
                current_date.get_meals_for_date(meals_table.meals_table)
                print(current_date)

            case "9":
                print("Exiting...")
                exit()

            case _:
                print("Invalid input. Please try again.")
                continue


if __name__ == "__main__":
    main()
