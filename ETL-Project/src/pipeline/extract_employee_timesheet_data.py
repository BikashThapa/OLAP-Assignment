import psycopg2


def connection_db():
    try:
        connection = psycopg2.connect(user="postgres",
                                    password="root2021",
                                    host="localhost",
                                    port=5432,
                                    database="healthCareSystem")
        print("Conencted to DB")
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)



def extract_employee_timesheet_data(filepath):
    with open(filepath,'r') as file:
        i =0
        for eachline in file:
            if i == 0:
                i += 1
                continue

            i += 1
            print(eachline)


if __name__ == "__main__":
   #  connection_db()
    extract_employee_timesheet_data("C:\\Users\\bikas\\Downloads\\Data_Enginner-Internship\\DBMS\\week3\\OLAP Design\\Assignmanets_all\\ETL-Project\\data\\timesheet_2021_07_24.csv")
    


    