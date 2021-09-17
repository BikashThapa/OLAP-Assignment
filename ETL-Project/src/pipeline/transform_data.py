
import sys
path = 'C:\\Users\\bikas\\Downloads\\Data_Enginner-Internship\\DBMS\\week3\\OLAP Design\\Assignmanets_all\\ETL-Project\\'
sys.path.append(path)

from src.util.connector import * 



def extract_department(cur,conn):
    sql1 = "DELETE FROM department"
    cur.execute(sql1)
    path = "C:\\Users\\bikas\\Downloads\\Data_Enginner-Internship\\DBMS\\week3\\OLAP Design\\Assignmanets_all\\ETL-Project\\src\\sql\\extract_department_from_raw_employee.sql"
    with open(path) as file:
        sql = "".join(file.readlines())
        cur.execute(sql)
        conn.close()




def extract_employee(cur,conn):
    path = "C:\\Users\\bikas\\Downloads\\Data_Enginner-Internship\\DBMS\\week3\\OLAP Design\\Assignmanets_all\\ETL-Project\\src\\sql\\transform_data_for_timesheet_table.sql"
    with open(path) as file:
        sql="".join(file.readlines)
        cur.execute(sql)
        conn.close()


def main():
    conn = connect()
    cur  = conn.cursor()
    extract_department(cur,conn)
    extract_employee(cur,conn)
if __name__  == "__main__":
    main()

