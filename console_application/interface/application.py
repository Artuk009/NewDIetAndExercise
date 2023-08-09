from connection.client_server_connection import ConnectionCredentials, Connection
from interface.printer import Printer
from interface.selections import Selections


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

            # Initialize Driver Classes
            printer = Printer()
            selection = Selections(connection)
            printer.print_date_heading(selection.current_date.date)
            choice = printer.print_options()

            match choice:
                case "1":
                    selection.show_ftable()

                case "2":
                    selection.show_dtable()

                case "3":
                    selection.insert_date()

                case "4":
                    selection.insert_food()

                case "5":
                    selection.insert_flmaster()

                case "6":
                    selection.show_bmtable()

                case "7":
                    selection.insert_bmeasurements()

                case "9":
                    print("Exiting...")
                    exit()

                case _:
                    print("Invalid input. Please try again.")
                    continue
