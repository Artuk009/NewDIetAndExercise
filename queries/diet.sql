CREATE TABLE dates_2023(
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE NOT NULL
);

CREATE TABLE meals(
    id INT AUTO_INCREMENT PRIMARY KEY,
    date_id INT NOT NULL,
    meal VARCHAR(255) NOT NULL,
    FOREIGN KEY (date_id) REFERENCES dates_2023(id)
);

CREATE TABLE foods(
    id INT AUTO_INCREMENT PRIMARY KEY,
    meal_id INT NOT NULL,
    food_name VARCHAR(255) NOT NULL,
    servings INT NOT NULL,
    carbs INT NOT NULL,
    fats INT NOT NULL,
    proteins INT NOT NULL,
    calories INT NOT NULL,
    FOREIGN KEY (meal_id) REFERENCES meals(id)
);

INSERT INTO dates_2023 (date, date, date) VALUES ('2023-06-20', '2023-06-20', '2023-06-21');

INSERT INTO meals (date_id, meal, meal, meal, meal) VALUES (1, 'Breakfast', 'Lunch', 'Dinner', 'Post-Workout');

SELECT f.food_name, m.meal, d.date
FROM foods f
INNER JOIN meals m on m.id = f.meal_id
INNER JOIN dates_2023 d on d.id = m.date_id;

UPDATE dates_2023 SET id = 1 WHERE date = '2023-06-20';

-- Remove id column from meals table
ALTER TABLE meals DROP COLUMN id;

DROP TABLE meals;

CREATE TABLE meals(
    id INT,
    date_id INT NOT NULL,
    meal VARCHAR(255) NOT NULL,
    FOREIGN KEY (date_id) REFERENCES dates_2023(id)
);

INSERT INTO meals (id, date_id, meal) VALUES (4, 1, 'Post-Workout');

UPDATE foods SET id = 3 WHERE food_name = 'Protein Powder';
UPDATE foods SET id = 2 WHERE food_name = 'Chips 1oz';

SELECT d.date, m.meal, f.food_name
FROM foods f
INNER JOIN meals m on m.id = f.meal_id
INNER JOIN dates_2023 d on d.id = m.date_id
GROUP BY d.date, m.meal, f.food_name;