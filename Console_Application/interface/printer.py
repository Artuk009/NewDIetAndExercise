class Printer:
    def print_date_heading(self, date):
        print()
        print("*" * 39)
        print("* Working with entries for", date, "*")
        print("*" * 39)
        print()

    def print_options(self):
        choice = input("Select an option: \n"
                       "[1] View Latest Food Entries \n"
                       "[2] View Dates Table \n"
                       "[3] Update the Date \n"
                       "[4] Log a New Food \n"
                       "[5] Add a New Food to the Food Master List \n"
                       "[6] View Latest Body Measurements \n"
                       "[7] Log New Body Measurements \n"
                       "[9] Exit \n")
        return choice
