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
        print(f"Latest {self.limit} entries:")
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
