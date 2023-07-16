import datetime as dt


def get_dates_table(connection):

    """Function to get the last 5 dates from the dates table"""

    cursor = connection.cursor(buffered=True)

    dates_table = []
    query = '''
    SELECT * 
    FROM dates_2023 
    ORDER BY id DESC
    LIMIT 5;'''
    cursor.execute(query)
    records = cursor.fetchall()
    for record in records:
        dates_table.append((record[0], record[1]))

    cursor.close()
    return dates_table


def show_dates_table(dates_table):
    print("Dates Table:")
    print("_" * 21)
    print("| {:<4} | {:<10} |".format("ID", "Date"))
    print("_" * 21)
    for entry in dates_table:
        print("| {:<4} | {} |".format(entry[0], entry[1]))
    print("_" * 21)


def set_date(day):

    """Function to set the date of the new entry"""

    year_month = dt.datetime.now().strftime("%Y-%m")

    # Confirm that the date is correct
    choice = input(f"Is {year_month}-{day} the correct date? [Y/N]: ")
    if choice.lower() == "y":
        date = f"{year_month}-{day}"
        return date
    elif choice.lower() == "n":
        set_date(day)
    else:
        print("Invalid input. Please try again.")
        set_date(day)


def set_new_date_id(dates_table):

    """Function to set the id of the new date"""

    new_id = dates_table[0][0] + 1
    return new_id


def get_latest_date_id(connection):

    """Function to get the id of the latest date"""

    cursor = connection.cursor(buffered=True)
    cursor.execute("SELECT id FROM dates_2023 ORDER BY id DESC LIMIT 1")
    latest_date_id = cursor.fetchone()[0]
    cursor.close()
    return latest_date_id


def get_latest_date(connection):

    """Function to get the latest date"""

    cursor = connection.cursor(buffered=True)
    cursor.execute("SELECT date FROM dates_2023 ORDER BY id DESC LIMIT 1")
    latest_date = cursor.fetchone()[0]
    cursor.close()
    return latest_date


class Dates:

    """Class to create a new date object"""

    def __init__(self, date_id, date):
        self.date_id = date_id
        self.date = date
        self.meals = {}

    def __str__(self):
        return f"{self.date} - {self.meals}"

    def get_meals_for_date(self, meals_table):

        """Function to get the meals for the date"""

        for meal in meals_table:
            self.meals[meal[2]] = meal[0]

    def add_date_to_db(self, connection):

        """Function to add the new date to the database"""

        cursor = connection.cursor(buffered=True)
        new_date = (self.date_id, self.date)

        # if date == new_date[1]:
        #     raise Exception("Date already entered")

        query = '''
        INSERT INTO dates_console_test (id, date) 
        VALUES (%s, %s)'''
        params = (new_date[0], new_date[1])
        cursor.execute(query, params)

        connection.commit()
        cursor.close()
        print("Date inserted to database")
