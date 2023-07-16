from diet_db import foods as f
from diet_db import dates as d
from diet_db import meals as m
from connection import client_server_connection as csc


def main():

    # Get user and password
    user, password = csc.get_user_and_password()

    # TODO: Creat function to update date table and meals table

    # Chose an option to execute
    while True:
        connection = csc.get_connection(user, password)
        choice = input("Select an option: \n"
                       "[1] View Latest Food Entries \n"
                       "[2] View Dates Table \n"
                       "[3] Add Date to Update \n"
                       "[4] Log a New Food \n"
                       "[9] Exit \n")

        dates_table = d.get_dates_table(connection)
        meals_table = m.get_meals_table(connection, d.get_latest_date_id(connection))

        match choice:
            case "1":
                entry_number = input("Enter the number of entries to view: ")
                f.get_latest_food_entries(connection, entry_number)

            case "2":
                d.show_dates_table(dates_table)

            case "3":
                day = input("Enter the day of the month: ")
                new_id = d.set_new_date_id(dates_table)
                new_date = d.set_date(day)
                print("The date has been set to", new_date, "with an id of", new_id)

                date_entry = d.Dates(new_id, new_date)
                date_entry.add_date_to_db(connection)

            case "4":
                # print(m.set_meal())
                # print(f.get_current_foods_count(connection))
                current_date = d.Dates(d.get_latest_date_id(connection), d.get_latest_date(connection))
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
