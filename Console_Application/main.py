from diet import Diet
import client_server_connection as csc
from dates import Dates


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
        match choice:
            case "1":
                get_foods = Diet()
                get_foods.get_latest_food_entries(connection, 5)
            case "2":
                get_dates = Dates()
                get_dates.get_dates(connection)
            case "3":
                add_date = Dates()
                date = add_date.set_date()
                print("The date has been set to", date)

                # TODO: Create function to add date to database

            case "9":
                print("Exiting...")
                exit()
            case _:
                print("Invalid input. Please try again.")
                continue


if __name__ == "__main__":
    main()
