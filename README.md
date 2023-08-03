# Diet and Exercise Data Analysis
### Introduction

In this project I use Pandas and Visualization libraries 
to explore and analyze personal diet and exercise data that I
have collected, and make adjustments accordingly based on my
findings. This is the planning phase of a grander project where
I plan to create web and mobile applications based on the logic 
from these notebooks. I am perfecting the database structure 
before I begin the development of the applications.

* The MySQL database is connected via the AWS RDS servers for more portability across devices. I grew tired of recreating the database localy.

### Console Application (Work in Progress)
* <a href="https://github.com/Artuk009/NewDIetAndExercise/tree/f533ecfa89425585c933a44fb48b37bf01862c80/Console_Application">Console Application</a> :
This is the implementation of the MySQL database structure that I designed in the analysis section. I am in the process
of converting the Pandas layout to a MySQL connector based application which should translate better to a web application.
I have been implementing unit testing as I go along to ensure that the application is working as intended with the 
unittest module.
* Tools: MySQL Connector, PyTest, and Unittest
* Sample body measurement entry output:
  ![Output #1](https://github.com/Artuk009/NewDIetAndExercise/blob/c7e5abd04e23f7c1e9aea7605bb5e33ce0a7ad9a/Visualizations/output1.png)
  ![Output #2](https://github.com/Artuk009/NewDIetAndExercise/blob/c7e5abd04e23f7c1e9aea7605bb5e33ce0a7ad9a/Visualizations/output2.png)

### Diet Analysis
* <a href="https://github.com/Artuk009/NewDIetAndExercise/blob/4d44f4d5e933581bf5e5c762a788e415a2d0ccd0/Diet_Analysis/diet_v6(Latest).ipynb">Diet Notebook</a> :
This notebook contains the code for the diet analysis. It is the latest
working version of the diet analysis code. The current features include
a MySQL database connection with a normalized database structure, the ability
to update entries within the database, and relevant calculations and 
visualizations for analysis. 
* <a href="https://github.com/Artuk009/NewDIetAndExercise/blob/90755b9eeae766faf609a628954ccc2c93134e78/Diet_Analysis/body_measurements_v2.ipynb">Body Measurements Notebook</a> :
This notebook has the code for reading and updating data from the body measurement table in the database. Then 
summary statistics and visualizations are created to analyze the data and determine what actions to take in terms
of adjusting the diet routine. There is a log entry at the end for tracking experiment time boxes and their
observed results.
* Tools: PyMySQL, Pandas, Seaborn, and SQLAlchemy.

### Queries
* <a href="https://github.com/Artuk009/NewDIetAndExercise/blob/90755b9eeae766faf609a628954ccc2c93134e78/Queries/aws_rds_MYSQL.sql">MySQL Queries</a> :
These are the queries I used to construct the schema for the MySQL database in addition to thr triggers and stored procedures
associated with the console application. I took a highly normalized approach to the database structure to ensure that the
tables are easily maintainable and scalable. I also included a trigger that automatically populates meal entries when a
date is logged because it wouldn't make sense not to have them in any scenario.
* Tools: MySQL and DataGrip Workbench (PyCharm Plugin)
* Database UML:<br>
![DB UML](https://github.com/Artuk009/NewDIetAndExercise/blob/d70365d5a6652dbf2906c8a765f948477cb86aef/Visualizations/DB_UML.png)


### Exercise Analysis (Suspended for Now)
