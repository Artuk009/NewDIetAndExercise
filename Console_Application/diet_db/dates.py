import datetime as dt


# Class to create and reference the dates in the database
def get_dates(connection):
    cursor = connection.cursor(buffered=True)

    # Function to get all dates from the database
    dates_table = []
    dates_query = '''
    SELECT * 
    FROM dates_2023 
    ORDER BY id DESC
    LIMIT 5;'''
    cursor.execute(dates_query)
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


def add_date_to_db(connection, date, dates_table):
    cursor = connection.cursor(buffered=True)
    new_date = [dates_table[0][0]+1, date]

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


class Dates:

    def __init__(self, date_id, date):
        self.date_id = date_id
        self.date = date

    def __str__(self):
        return f"{self.date}"


