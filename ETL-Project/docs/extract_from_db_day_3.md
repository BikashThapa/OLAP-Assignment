# Data extraction from one data source to another data sources
On day 3, the data from on database source is extracted to another data source using SQL quereis from pipeline.

## Steps in data extraction process
- import necessary packages 
- connect to the source database 
- connect to destination database
- Read required data from source table
-For each record
    -  Prepare insert statement and run the insert statement
- close the source and destination connection 

# steps done in creatig a pipeline and other folders


- sql
    - Here, we have created a sql folder for storing all sql files that need to be quired along the process of extraction.We have added the insert_into_extract-db and extract_sales_data. Here in the extraction process from sales data like users and other, we have used the JOIN statement on the matching field and returned the required new db column in same manner. The remaining quantity is calculted by subtracting sales quantity from product quantity.

- util 
    - Here, the connection is established and two connection is made, one for source and another from destination. The source db is testEcommerce database and destination database is healthCareSystem

- pipeline
    - we have added one pipeline for extraction process named as extraction_from_db.py. The pipeline program connects to the database, reads the required files from source database and import into the destination database tables as mentioned.