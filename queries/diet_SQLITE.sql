-- Create the dates table for the database
CREATE TABLE dates_2023(
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE NOT NULL
);

-- Create the meals table for the database
CREATE TABLE meals(
    id INT AUTO_INCREMENT PRIMARY KEY,
    date_id INT NOT NULL,
    meal VARCHAR(255) NOT NULL,
    FOREIGN KEY (date_id) REFERENCES dates_2023(id)
);

-- Create the foods table for the database
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

-- Insert dates into dates table
INSERT INTO dates_2023 (date, date, date) VALUES ('2023-06-20', '2023-06-20', '2023-06-21');

INSERT INTO meals (date_id, meal, meal, meal, meal) VALUES (1, 'Breakfast', 'Lunch', 'Dinner', 'Post-Workout');

-- Inspect some of the data
SELECT f.food_name, m.meal, d.date
FROM foods f
INNER JOIN meals m on m.id = f.meal_id
INNER JOIN dates_2023 d on d.id = m.date_id;

-- Update mistakes in dates table
UPDATE dates_2023 SET id = 1 WHERE date = '2023-06-20';

-- Remove id column from meals table
ALTER TABLE meals DROP COLUMN id;

-- Remove id column from foods table
DROP TABLE meals;
CREATE TABLE meals(
    id INT,
    date_id INT NOT NULL,
    meal VARCHAR(255) NOT NULL,
    FOREIGN KEY (date_id) REFERENCES dates_2023(id)
);

-- Insert an entry into meals table
INSERT INTO meals (id, date_id, meal) VALUES (4, 1, 'Post-Workout');

-- Update foods table with new id's
UPDATE foods SET id = 3 WHERE food_name = 'Protein Powder';
UPDATE foods SET id = 2 WHERE food_name = 'Chips 1oz';

-- Get all foods from dates_2023 by date and meal
SELECT d.date, m.meal, f.food_name
FROM meals m
INNER JOIN foods f on f.meal_id = m.id
INNER JOIN dates_2023 d on d.id = m.date_id
WHERE d.date = '2023-06-28'
ORDER BY f.id;

-- Create new meal table with id as primary key
CREATE TABLE new_meals(
    id INT AUTO_INCREMENT PRIMARY KEY,
    date_id INT NOT NULL,
    meal VARCHAR(255) NOT NULL,
    FOREIGN KEY (date_id) REFERENCES dates_2023(id)
);


