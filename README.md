# Diet and Exercise Data Analysis
### Introduction

In this project I use Pandas and Visualization libraries 
to explore and analyze personal diet and exercise data that I
have collected, and make adjustments accordingly based on my
findings. This is the planning phase of a grander project where
I plan to create web and mobile applications based on the logic 
from these notebooks. I am perfecting the database structure 
before I begin the development of the applications.

* The MySQL database is connected via the AWS RDS servers for portability across devices.

### Console Application (Work in Progress)
* <a href="https://github.com/Artuk009/NewDIetAndExercise/tree/afbcd3a1d9b7df15b1d00146573d8940bd5a243d/Console_Application">Console Application</a> :
This is the implementation of the MySQL database structure that I designed in the analysis section. I am in the process
of converting the Pandas layout to a MySQL connector based application which should translate better to a web application.
I have been implementing unit testing as I go along to ensure that the application is working as intended with the 
unittest module.
* Tools: MySQL Connector, PyTest, and Unittest

### Diet Analysis
* <a href="https://github.com/Artuk009/NewDIetAndExercise/blob/b2cc8f0e31b921dee4c4c3d52a24a3e775cc2959/Diet_Stuff/diet_v5(Latest).ipynb">Diet Notebook</a> :
This notebook contains the code for the diet analysis. It is the latest
working version of the diet analysis code. The current features include
a MySQL database connection with a normalized database structure, the ability
to update entries within the database, and relevant calculations and 
visualizations for analysis. 
* <a href="https://github.com/Artuk009/NewDIetAndExercise/blob/4ebacaece70afb677174cf85f8ea4cc9c694202a/Diet_Analysis/body_measurements_v2.ipynb">Body Measurements Notebook</a> :
This notebook has the code for reading and updating data from the body measurement table in the database. Then 
summary statistics and visualizations are created to analyze the data and determine what actions to take in terms
of adjusting the diet routine. There is a log entry at the end for tracking experiment time boxes and their
observed results.
* Tools: PyMySQL, Pandas, Seaborn, and SQLAlchemy.

### Queries
* <a href="https://github.com/Artuk009/NewDIetAndExercise/blob/b2cc8f0e31b921dee4c4c3d52a24a3e775cc2959/Queries/diet_MYSQL.sql">MySQL Queries</a> :
These are the queries I used to construct the schema for the MySQL database in addition to thr triggers and stored procedures
associated with the console application. I took a highly normalized approach to the database structure to ensure that the
tables are easily maintainable and scalable. I also included a trigger that automatically populates meal entries when a
date is logged because it wouldn't make sense not to have them in any scenario.
* Tools: MySQL and DataGrip Workbench (PyCharm Plugin)

### Exercise Analysis (Suspended for Now)
