class BodyMeasurementsTable:

    """Class to create body measurements table object"""

    def __init__(self, connection):
        self.connection = connection
        self.limit = 5
        self.body_measurements_table = []

    def get_body_measurements_table(self, limit):

        """Method to get the latest body measurements from the database"""

        self.limit = limit
        cursor = self.connection.cursor(buffered=True)
        cursor.callproc("GetBodyMeasurementsByDate")
        results = next(cursor.stored_results())
        dataset = results.fetchmany(self.limit)
        for data in dataset:
            self.body_measurements_table.append(data)
        cursor.close()
        return self.body_measurements_table

    def show_body_measurements_table(self):

        """Method to show the body measurements table"""

        print()
        print(f"{self.limit} latest body measurement entries:")
        print("*" * 77)
        print("* {:<3} | {:<10} | {} | {} | {} | {} | {} *".format(
            'ID', 'Date', 'Weight', 'Body Fat %', 'Muscle Mass', 'Fat Mass', 'Workout'
        ))
        print("*" * 77)
        for data in self.body_measurements_table:
            print("* {:<3} | {} | {:<6} | {:<10} | {:<11} | {:<8} | {:<7} *".format(
                data[0], data[1], data[2], data[3], data[4], data[5], data[6]))
        print("*" * 77)
        print()


class MeasurementCount:

    """Class to create measurement count object"""

    def __init__(self, connection):
        self.connection = connection
        self.measurement_count = 0

    def get_measurement_count(self):

        """Method to get the latest measurement count from the database"""

        cursor = self.connection.cursor(buffered=True)
        cursor.execute("SELECT * FROM body_measurements")
        results = cursor.fetchall()
        for result in results:
            self.measurement_count += 1
        cursor.close()
        return self.measurement_count


class BodyMeasurements:

    """Class to create and store body  measurement entries in the database"""

    def __init__(self, connection, measurement_id, date_id, measurements):
        self.connection = connection
        self.measurement_id = measurement_id
        self.date_id = date_id
        self.measurements = measurements

    def add_measurements(self):

        """Method to add a new measurement entry to the database"""

        cursor = self.connection.cursor(buffered=True)
        cursor.execute("INSERT INTO body_measurements VALUES (%s, %s, %s)",
                       (self.measurement_id, self.date_id, self.measurements))
        self.connection.commit()
        cursor.close()
        print(f"New body measurement entry added to database")
