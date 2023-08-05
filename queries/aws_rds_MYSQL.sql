create database diet;

use diet;

-- Generated Table DDls from previous server --
create table dates_2023
(
    id   int auto_increment
        primary key,
    date date not null
);

create table body_measurements
(
    id           int auto_increment
        primary key,
    date_id      int  not null,
    measurements json null,
    constraint body_measurements_ibfk_1
        foreign key (date_id) references dates_2023 (id)
);

create index date_id
    on body_measurements (date_id);

create table food_list_master
(
    id             int auto_increment
        primary key,
    food_name      varchar(255) not null,
    nutrition_info json         null,
    constraint food_name
        unique (food_name)
);

create table foods
(
    id             int auto_increment
        primary key,
    meal_id        int          not null,
    food_name      varchar(255) not null,
    servings       int          not null,
    nutrition_info json         null,
    constraint foods_ibfk_1
        foreign key (meal_id) references meals (id)
);

create index meal_id
    on foods (meal_id);

create table meals
(
    id      int auto_increment
        primary key,
    date_id int          not null,
    meal    varchar(255) not null,
    constraint meals_ibfk_1
        foreign key (date_id) references dates_2023 (id)
);

create index date_id
    on meals (date_id);

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

-- Create procedure to get specific food info from food list master
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

-- Create a new user with only necessary permissions for the application --
CREATE USER 'diet_user'@'%' IDENTIFIED BY 'diet_user';
GRANT SELECT, INSERT, UPDATE, DELETE, EXECUTE ON diet.* TO 'diet_user'@'%';
show grants for 'diet_user';