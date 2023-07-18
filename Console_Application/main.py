from diet_db import foods as f
from diet_db import meals as m
from diet_db.dates import\
    Dates, InsertDate, DatabaseDate, DatabaseDateID, SetNewDate, SetNewDateID, DatesTable
from connection.client_server_connection import \
    ConnectionCredentials, Connection

# TODO: Adjust tests for dates module
# TODO: Apply SOLID principles to meals module


def main():

    # Get credentials for database
    credentials = ConnectionCredentials()

    # Chose an option to execute
    while True:
        connection = Connection(
            credentials.get_username(),
            credentials.get_password()
        ).get_connection()

        choice = input("Select an option: \n"
                       "[1] View Latest Food Entries \n"
                       "[2] View Dates Table \n"
                       "[3] Add Date to Update \n"
                       "[4] Log a New Food \n"
                       "[9] Exit \n")

        dates_table = DatesTable(connection)
        dates_table.get_dates_table()
        meals_table = m.get_meals_table(
            connection, DatabaseDateID(connection).get_latest_date_id()
        )

        match choice:
            case "1":
                entry_number = input("Enter the number of entries to view: ")
                f.get_latest_food_entries(connection, int(entry_number))

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
                # print(m.set_meal())
                # print(f.get_current_foods_count(connection))
                current_date = Dates(
                    DatabaseDateID(connection).get_latest_date_id(),
                    DatabaseDate(connection).get_latest_date()
                )
                current_date.get_meals_for_date(meals_table)
                print(current_date)

            case "9":
                print("Exiting...")
                exit()

            case _:
                print("Invalid input. Please try again.")
                continue


if __name__ == "__main__":
    main()
