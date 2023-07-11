import datetime as dt

# Class to create and reference the dates in the database
class Dates:

    class Date:
        def __init__(self, date_id, date):
            self.date_id = date_id
            self.date = date

        def __str__(self):
            return f"{self.date}"

    # Function to get last five dates from the database
    def get_dates(self, connection):
        cursor = connection.cursor(buffered=True)

        # Function to get all dates from the database
        dates_query = '''
        SELECT * 
        FROM dates_2023 
        ORDER BY id DESC
        LIMIT 5;'''
        cursor.execute(dates_query)
        records = cursor.fetchall()
        for record in records:
            print(f"[Id: {record[0]}] - {record[1]}")

        cursor.close()

    # Function to set the date for the user to log their intake
    def set_date(self):
        year_month = dt.datetime.now().strftime("%Y-%m")
        day = input("Enter the day of the month: ")

        # Confirm that the date is correct
        choice = input(f"Is {year_month}-{day} the correct date? [Y/N]: ")
        if choice.lower() == "y":
            date = f"{year_month}-{day}"
            return date
        elif choice.lower() == "n":
            self.set_date()
        else:
            print("Invalid input. Please try again.")
            self.set_date()
