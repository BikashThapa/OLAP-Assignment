
import json
import psycopg2


def connection_db():
    return psycopg2.connect(user="postgres",
                                    password="root2021",
                                    host="localhost",
                                    port=5432,
                                    database="healthCareSystem")
        

    



def extract_employee_data(filepath):
    conn = connection_db()
    cursor = conn.cursor()

    #if the file is json
    if ".json" in filepath:
        with open(filepath,'r') as file:
            data=json.load(file)
    

    #query to remove prevous data if present in raw_employee
    delete_query = "DELETE FROM raw_employee"
    cursor.execute(delete_query)
    conn.commit


    #query to insert the data into raw_employee
    import_query = ''' INSERT INTO raw_employee VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s %s); ''' 
    
    data_all=[]
    for item in data:
        row=[]
        for value in item.values():
            row.append(value)
        
        data_all.append(row)
    cursor.execute(import_query)
    conn.commit()


if __name__ == "__main__":

    extract_employee_data("C:\\Users\\bikas\\Downloads\\Data_Enginner-Internship\\DBMS\\week3\\OLAP Design\\Assignmanets_all\\ETL-Project\\data\\employee_2021_08_01.json")
    
    