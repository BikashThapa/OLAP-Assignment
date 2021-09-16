import sys

path = 'C:\\Users\\bikas\\Downloads\\Data_Enginner-Internship\\DBMS\\week3\\OLAP Design\\Assignmanets_all\\ETL-Project\\'
sys.path.append(path)

from src.util.connector import * 

def extract_employee_timesheet(filepath):
    connection = connect()
    cursor = connection.cursor()

    delete_records('..\\src\\sql\\delete_raw_employee_timesheet_data.sql')

    copy_from_csv = '''
        COPY raw_timesheet
        FROM %s
        WITH (
            FORMAT TEXT,
            DELIMITER ','
        );
    '''

    cursor.execute(copy_from_csv,(filepath,))
    connection.commit()
    cursor.close()
    connection.close()


if __name__ == "__main__":
    file_paths = ['..\\data\\timesheet_2021_05_23.csv','..\\ata\\timesheet_2021_06_23.csv','..\\data\\timesheet_2021_07_24.csv']

    for filepath in file_paths:
        extract_employee_timesheet(filepath)

    