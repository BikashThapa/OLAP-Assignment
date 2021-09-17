# Data transformation from raw employee timesheet, raw employee and department
On day 4, The tranformation process is done for storing the table into the timesheet table.

## Steps in data tranformation process

- In first step, the data is loaded from different sources  for reading.
- Then the transformation process is carried out as required by business or client.
- The timesheet table is created so that we can store the trasformed data into the database for future use.


## Following process is carried out to perform the transformation process 
- Employee_id from the employee raw data.
- shift_start_time is calculated by finding the time from punch_in_time column
- shift_out_time is calculated by finding the time from punch_out_time column
- sift date is calculated by using punch_apply_date 
- shift_type is calculated by using punch_in_time as that ranges from differnt time period and name them as MORNING, DAY or EVENING
- attendance is calculated by using paycode ccolumn and checking either the row contains ABSENT in the column or not.
- has_taken_break is calculated by comparing above column with BREAK and returns 1 if yes else 0
- break_hour, charge_hour, was_on_call and on_call hour is calculated by using WHEN statement and at last casting them as a flot.


# steps done in creatig a pipeline and other folders

- sql
    - Here, we have created a first department table for the department storage so that that's primary key of department can be used in another table for the foreign key.
    -The timesheet table is created for storing the transformed data into the databae.
    - The transformed data process is done in transform_data_for_timesheet_table.sql
        - Here, different approaches are used for tranformation of data into the required format and datatypes as required.

- pipeline
    - we have created the transform_data.py for the transformation and storage of data into the database. The transformed database is used for the future analytical processing and other business decisions by the business or client.