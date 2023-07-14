from diet_db import foods as f
from diet_db import meals as m
from connection import client_server_connection as csc
from diet_db import dates as d


def main():

    # Get user and password
    user, password = csc.get_user_and_password()

    # TODO: Create function to get master list of foods from database
    # TODO: Creat function to update date table and meals table

    # Chose an option to execute
    while True:
        connection = csc.get_connection(user, password)
        choice = input("Select an option: \n"
                       "[1] View Latest Food Entries \n"
                       "[2] View Dates Table \n"
                       "[3] Add Date to Update \n"
                       "[9] Exit \n")

        dates_table = d.get_dates(connection)

        match choice:
            case "1":
                f.get_latest_food_entries(connection, 5)
            case "2":
                d.show_dates_table(dates_table)
            case "3":
                date = d.set_date()
                print("The date has been set to", date)

                d.add_date_to_db(connection, date, dates_table)
            case "9":
                print("Exiting...")
                exit()
            case _:
                print("Invalid input. Please try again.")
                continue


if __name__ == "__main__":
    main()
