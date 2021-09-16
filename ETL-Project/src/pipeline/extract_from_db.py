
import sys
path = 'C:\\Users\\bikas\\Downloads\\Data_Enginner-Internship\\DBMS\\week3\\OLAP Design\\Assignmanets_all\\ETL-Project\\'
sys.path.append(path)
from src.util.connector import * 



def extract_data_db():
    source_conn = connect1()
    dest_conn = connect()

    source_cursor =source_conn.cursor()
    dest_cursor = dest_conn.cursor()

    with open('C:\\Users\\bikas\\Downloads\\Data_Enginner-Internship\\DBMS\\week3\\OLAP Design\\Assignmanets_all\\ETL-Project\\src\\sql\\delete_sales_data.sql') as deletefile:
        delete= "".join(deletefile.readlines())
        dest_cursor.execute(delete)
        dest_conn.commit()
       


    with open('C:\\Users\\bikas\\Downloads\\Data_Enginner-Internship\\DBMS\\week3\\OLAP Design\\Assignmanets_all\\ETL-Project\\src\\sql\\extract_sales_data.sql') as sqlFile:
        sqlquery= "".join(sqlFile.readlines())
        source_cursor.execute(sqlquery)
        result = source_cursor.fetchall()
        sql ='''
        INSERT INTO sales_data (user_id,username ,product_id ,product_name, category_id,category_name, current_price ,sold_price ,sold_quantity, remainig_quantity,sales_date)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
        
        '''
        for row in result:
            dest_cursor.execute(sql,row)
            dest_conn.commit()
    source_cursor.close()
    dest_cursor.close()
    source_conn.close()
    dest_conn.close()   
    



if __name__  == "__main__":
    extract_data_db()


