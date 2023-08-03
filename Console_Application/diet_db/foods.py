class FoodsTable:

    """Class to create a foods table object"""

    def __init__(self, connection):
        self.connection = connection
        self.limit = 5
        self.foods_table = []

    def get_foods_table(self, connection, limit):

        """Method to get the latest food entries from the database"""

        cursor = connection.cursor(buffered=True)
        cursor.callproc("GetFoodsByMealAndDateFromFoods")
        results = next(cursor.stored_results())
        dataset = results.fetchmany(limit)
        for data in dataset:
            self.foods_table.append(data)

        cursor.close()
        return self.foods_table

    def show_foods_table(self):

        """Method to show the foods table"""

        print()
        print("Latest 5 entries:")
        print("*" * 93)
        print("* {:<3} | {:<10} | {:<15} | {:<20} | {} | {:<4} | {:<4} | {:<4} | {:<4} *".format(
            'ID', 'Date', 'Meal', 'Food', 'S', 'Carb', 'Fats', 'Prot', 'Cals'
        ))
        print("*" * 93)
        for data in self.foods_table:
            print("* {:<3} | {} | {:<15} | {:<20} | {} | {:<4} | {:<4} | {:<4} | {:<4} *".format(
                data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8]))
        print("*" * 93)
        print()


class FoodMasterList:

    """Class to create a food master list object"""

    def __init__(self, connection):
        self.connection = connection
        self.food_master_list = []

    def get_food_master_list(self):

        """Method to get the food master list from the database"""

        cursor = self.connection.cursor(buffered=True)
        query = "SELECT * FROM food_list_master"
        cursor.execute(query)
        results = cursor.fetchall()
        for result in results:
            self.food_master_list.append(result)
        cursor.close()
        return self.food_master_list

    def get_names(self):
        names = []
        for food in self.food_master_list:
            names.append(food[1])
        return names


class GetNutritionInfo:

    """Class to get the nutrition info for a food entry"""

    def __init__(self, food_name, connection):
        self.food_name = food_name
        self.connection = connection

    def get_nutrition_info(self):

        """Method to get the nutrition info for a food entry"""

        food_master_list = FoodMasterList(self.connection).get_food_master_list()
        for food in food_master_list:
            if food[1] == self.food_name:
                return food[2]
        return None


class FoodCount:

    """Class to create a food count object"""

    def __init__(self, connection):
        self.connection = connection
        self.food_count = 0

    def get_food_count(self):

        """Method to get the food count from the database"""

        cursor = self.connection.cursor(buffered=True)
        cursor.execute("SELECT * FROM foods")
        results = cursor.fetchall()
        for result in results:
            self.food_count += 1
        cursor.close()
        return self.food_count

    def get_food_list_master_count(self):

        """Method to get the food count from the database"""

        cursor = self.connection.cursor(buffered=True)
        cursor.execute("SELECT * FROM food_list_master")
        results = cursor.fetchall()
        for result in results:
            self.food_count += 1
        cursor.close()
        return self.food_count


class Foods:

    """Class to create and store food entries in the database"""

    def __init__(self, *column_headers):
        if len(column_headers) == 5:
            self.food_id = column_headers[0]
            self.meal_id = column_headers[1]
            self.food_name = column_headers[2]
            self.servings = column_headers[3]
            self.nutrition_info = column_headers[4]
        elif len(column_headers) == 3:
            self.food_id = column_headers[0]
            self.food_name = column_headers[2]
            self.nutrition_info = column_headers[4]
        else:
            raise ValueError("Incorrect number of arguments")

    def __str__(self):
        return f"{self.food_id} - {self.meal_id} - {self.food_name} - {self.nutrition_info}"

    def add_food(self, connection):
        cursor = connection.cursor(buffered=True)
        new_food = (self.food_id, self.meal_id, self.food_name, self.servings, self.nutrition_info)
        query = '''
        INSERT INTO foods(id, meal_id, food_name, servings, nutrition_info)
        VALUES (%s, %s, %s, %s, %s)
        '''
        cursor.execute(query, new_food)
        connection.commit()
        cursor.close()
        print("Food inserted to database")

    def add_food_to_food_list_master(self, connection):
        cursor = connection.cursor(buffered=True)
        new_food_master_entry = (self.food_id, self.food_name, self.nutrition_info)
        query = '''
        INSERT INTO food_list_master(id, food_name, nutrition_info)
        VALUES (%s, %s, %s)
        '''
        cursor.execute(query, new_food_master_entry)
        connection.commit()
        cursor.close()
        print("Food inserted to database")
