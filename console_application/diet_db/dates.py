import datetime as dt


class DatesTable:

    """Class to create a dates table object"""

    def __init__(self, connection):
        self.connection = connection
        self.dates_table = []

    def get_dates_table(self):
        cursor = self.connection.cursor(buffered=True)

        query = '''
        SELECT * 
        FROM dates_2023 
        ORDER BY id DESC
        LIMIT 5;'''
        cursor.execute(query)
        records = cursor.fetchall()
        for record in records:
            self.dates_table.append((record[0], record[1]))

        cursor.close()
        return self.dates_table

    def show_dates_table(self):
        print()
        print("Dates Table:")
        print("*" * 21)
        print("* {:<4} | {:<10} *".format("ID", "Date"))
        print("*" * 21)
        for entry in self.dates_table:
            print("* {:<4} | {} *".format(entry[0], entry[1]))
        print("*" * 21)
        print()


class SetNewDate:

    """Class to set the date of the new entry"""

    def __init__(self, day):
        self.day = day

    def set_new_date(self):

        """Method to set the date of the new entry"""

        year_month = dt.datetime.now().strftime("%Y-%m")

        # Confirm that the date is correct
        choice = input(f"Is {year_month}-{self.day} the correct date? [Y/N]: ")
        if choice.lower() == "y":
            date = f"{year_month}-{self.day}"
            return date
        elif choice.lower() == "n":
            self.set_new_date()
        else:
            print("Invalid input. Please try again.")
            self.set_new_date()


class SetNewDateID:

    """Class to set the id of the new date"""

    def __init__(self, dates_table):
        self.dates_table = dates_table

    def set_new_date_id(self):
        new_id = self.dates_table[0][0] + 1
        return new_id


class DatabaseDateID:

    """Class to get the id of the latest date"""

    def __init__(self, connection):
        self.connection = connection

    def get_latest_date_id(self):
        cursor = self.connection.cursor(buffered=True)
        cursor.execute("SELECT id FROM dates_2023 ORDER BY id DESC LIMIT 1")
        latest_date_id = cursor.fetchone()[0]
        cursor.close()
        return latest_date_id


class DatabaseDate:

    """Class to get the date of the latest date"""

    def __init__(self, connection):
        self.connection = connection

    def get_latest_date(self):
        cursor = self.connection.cursor(buffered=True)
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
        for meal in meals_table:
            self.meals[meal[2]] = meal[0]


class InsertDate:

    """Class to insert a new date into the database"""

    def __init__(self, date_id, date):
        self.date_id = date_id
        self.date = date

    def add_date_to_db(self, connection):
        cursor = connection.cursor(buffered=True)
        new_date = (self.date_id, self.date)

        # if date == new_date[1]:
        #     raise Exception("Date already entered")

        query = '''
        INSERT INTO dates_2023 (id, date) 
        VALUES (%s, %s)'''
        params = (new_date[0], new_date[1])
        cursor.execute(query, params)

        connection.commit()
        cursor.close()
        print("Date inserted to database")
