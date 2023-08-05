

class Selections:
    def show_ftable(self, foods_table):
        entry_number = input("Enter the number of entries to view: ")
        foods_table.get_foods_table(int(entry_number))
        foods_table.show_foods_table()

    def show_bmtable(self, body_measurements_table):
        entry_number = input("Enter the number of entries to view: ")
        body_measurements_table.get_body_measurements_table(int(entry_number))
        body_measurements_table.show_body_measurements_table()