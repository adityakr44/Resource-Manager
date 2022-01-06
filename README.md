# Resource-Manager
Develop a project to go through a query written in the form of Python code and find out the number of times a resource (for example a file) is accessed. 


In this project, we take query from the code and solve the query using the files that we have prepared before the making the code. After running the queries, the output will show the result of the queries and also the number of times each of the files was accessed during the queries.

In the files, we have taken SGPAs of students of all departments and all years as data files of last three semesters. We have folders in the names of all departments and in each department there are 4 folders of each year. 
•	Now through queries given in the code we will perform operations on these files. In this project we are going to perform two operations, first checking the passing and failing status, second putting people in categories of their grades. 
•	For example: In our 3rd query we ask for the number of students passed particularly of IT department all years. So it checks the files of only IT folder and access the files of only that folder. Let’s say for other example, in our 4th query we want the pass categories of IT department of only 2nd year, so it will access only the file of 2nd year in IT folder.
•	For performing the above mentioned operations we made two python code files. 1st one is res_manager.py which will contain all the functions to run the operations and will work as a module for the 2nd python file named main.py , which contains the query and log files operations.
•	And after solving all the queries it will show the result of the queries and the number of times it was accessed and stores this data in the log file.
