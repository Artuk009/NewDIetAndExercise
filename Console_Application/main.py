import diet as d
import client_server_connection as csc


def main():

    # Get user and password

    user, password = csc.get_user_and_password()

    # TODO: Create function to get master list of foods from database
    # TODO: Creat function to update date table and meals table

    # Chose an option to execute
    while True:
        connection = csc.get_connection(user, password)
        choice = input("Select an option: [1] View Latest Food Entries [9] Exit: ")
        match choice:
            case "1":
                d.Diet.get_latest_food_entries(connection, 5)
            case "9":
                print("Exiting...")
                exit()
            case _:
                print("Invalid input. Please try again.")
                continue


if __name__ == "__main__":
    main()
