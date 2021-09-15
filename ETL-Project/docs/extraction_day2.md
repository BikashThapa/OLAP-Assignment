# Data extraction from differnet Sources - Day 2
On day 2, the data from different sources are populated into the raw_employee and raw_epmloyee_timesheet table from different sources like csv, xml and json file format. 

we have already craeted our schema for the database and we have used all datatypes as VARCHAR as the format might changes in the process of data collection.

## Steps in data extraction process
- import necessary packages 
- connect to the database 
- open different files from the different path as required
-  For each file prepare insert query and insert into db
- commit the query
- close connection and cursor.

# steps done in creatig a pipeline and other folders
- data
    - Here, all the required data that need to be imported must be placed or we need to take the file path of that specific required data.

- sql
    - Here, we have created a sql folder for storing all sql files that need to be quired along the process of extraction.

- util 
    - Here, the connection is established and delete query is written in a function which later can be used by other files as well.

- pipeline
    - we have created  two files for each raw_emplyee data and raw_employee_timesheet data.
         - In the raw_employee file, we have populated data from json and xml file resp into the schema.
         - In the raw_employee_timesheet, we have populated the timesheet of employee which was in the format of csv file.