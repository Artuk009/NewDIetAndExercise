CREATE DATABASE diet;

USE diet;

-- TABLES --

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

-- Create the body measurements table for the database
CREATE TABLE body_measurements(
    id INT AUTO_INCREMENT PRIMARY KEY,
    date_id INT NOT NULL,
    body_weight INT NOT NULL,
    body_fat REAl NOT NULL,
    muscle_mass REAL NOT NULL,
    fat_mass REAL NOT NULL,
    workout_type VARCHAR(255) NOT NULL,
    FOREIGN KEY (date_id) REFERENCES dates_2023(id)
);

-- Create the food list master table for the database
CREATE TABLE food_list_master(
    id INT AUTO_INCREMENT PRIMARY KEY,
    food_name VARCHAR(255) NOT NULL UNIQUE,
    carbs INT NOT NULL,
    fats INT NOT NULL,
    proteins INT NOT NULL,
    calories INT NOT NULL
);

-- PROCEDURES --

-- Create procedure to get all foods and meals for all dates
CREATE PROCEDURE GetFoodsByMealAndDate()
SELECT f.id, d.date, m.meal, f.food_name, f.servings, f.carbs, f.fats, f.proteins, f.calories
FROM meals m
INNER JOIN foods f on f.meal_id = m.id
INNER JOIN dates_2023 d on d.id = m.date_id
ORDER BY f.id;

CALL GetFoodsByMealAndDate();

-- Create procedure to get all foods and meals for all dates from foods json
CREATE PROCEDURE GetFoodsByMealAndDateFromFoods()
SELECT f.id, d.date, m.meal, f.food_name, f.servings, f.nutrition_info->'$.carbs' AS carbs,
       f.nutrition_info->'$.fats' AS fats, f.nutrition_info->'$.proteins' AS proteins,
       f.nutrition_info->'$.calories' AS calories
FROM meals m
INNER JOIN foods f on f.meal_id = m.id
INNER JOIN dates_2023 d on d.id = m.date_id
ORDER BY f.id;

CALL GetFoodsByMealAndDateFromFoods();

-- Create procedure to get food from food list master by name
DELIMITER //
CREATE PROCEDURE GetFoodInfo(foodName VARCHAR(255))
BEGIN
    SELECT food_name, carbs, fats, proteins, calories
    FROM food_list_master
    WHERE food_name = foodName;
END //
DELIMITER ;

CALL GetFoodInfo('Ramen');

-- Create procedure to get food from food list master json by name
DELIMITER //
CREATE PROCEDURE GetFoodInfoFromFoodListMaster(foodName VARCHAR(255))
BEGIN
    SELECT food_name, nutrition_info
    FROM food_list_master
    WHERE food_name = foodName;
END //
DELIMITER ;

CALL GetFoodInfoFromFoodListMaster('Ramen');

-- Create procedure to get all body measurements json for all dates
CREATE PROCEDURE GetBodyMeasurementsByDate()
SELECT b.id, d.date, b.measurements->'$.body_weight' AS body_weight,
       b.measurements->'$.body_fat' AS body_fat, b.measurements->'$.muscle_mass' AS muscle_mass,
       b.measurements->'$.fat_mass' AS fat_mass, b.measurements->'$.workout_type' AS workout_type
FROM body_measurements b
INNER JOIN dates_2023 d on d.id = b.date_id
ORDER BY b.id;

CALL GetBodyMeasurementsByDate();
drop procedure GetBodyMeasurementsByDate;
-- JSON CONVERSIONS --

-- Convert food properties to JSON in food list master
SELECT f.id, f.food_name,
       JSON_OBJECT('carbs', f.carbs, 'fats', f.fats, 'proteins', f.proteins, 'calories', f.calories) AS
         nutrition_info
FROM food_list_master f;

-- Convert food properties to JSON in foods
SELECT f.id, f.meal_id, f.food_name, f.servings,
       JSON_OBJECT('carbs', f.carbs, 'fats', f.fats, 'proteins', f.proteins, 'calories', f.calories) AS
         nutrition_info
FROM foods f;

-- Convert body measurements to JSON
SELECT b.id, b.date_id,
       JSON_OBJECT('body_weight', b.body_weight, 'body_fat', b.body_fat, 'muscle_mass', b.muscle_mass,
                   'fat_mass', b.fat_mass, 'workout_type', b.workout_type) AS body_measurements
FROM body_measurements b;

-- TRIGGERS --

-- Create trigger to update meals table when a new date is added
DELIMITER //
CREATE TRIGGER AddMealsOnDateAdd
AFTER INSERT ON dates_2023
FOR EACH ROW
BEGIN
    INSERT INTO meals (date_id, meal)
    VALUES (NEW.id, 'Breakfast'), (NEW.id, 'Lunch'), (NEW.id, 'Dinner'), (NEW.id, 'Post-Workout');
END //
DELIMITER ;

show triggers;








