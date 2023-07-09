import diet
from diet import Diet as d


def main():
    food = d.Foods(1, 1, "Apple", 1, {"fats": 95, "carbs": 25, "calories": 0.5, "proteins": 0.3})
    meal = d.Meals(1, 1, "Breakfast")
    date = d.Dates(1, "2021-04-01")
    print(f'[{date}] {meal}: {food}')

    conn = diet.get_connection()
    cursor = conn.cursor()
    diet.get_limited_rows(cursor, 5)

    # TODO: Create function to get master list of foods from database
    # TODO: Creat function to update date table and meals table


if __name__ == "__main__":
    main()
