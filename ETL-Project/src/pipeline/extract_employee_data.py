import sys
path = 'C:\\Users\\bikas\\Downloads\\Data_Enginner-Internship\\DBMS\\week3\\OLAP Design\\Assignmanets_all\\ETL-Project\\'
sys.path.append(path)
import json
import xmltodict
from src.util.connector import * 


def extract_json_data(filepath):
    connection = connect()
    cursor = connection.cursor()

    delete_records('..\\src\\sql\\delete_raw_employee_data.sql')

    with open(filepath) as json_data:
        record_list = json.load(json_data)

    with open('..\\src\\sql\\import_raw_employee_data.sql') as insert_data:
        insert_file_query = "".join(insert_data.readlines())
        cursor.executemany(insert_file_query, record_list)
        connection.commit()
    cursor.close()
    connection.close()


def extract_xml_data(filepath):
    connection = connect()
    cursor = connection.cursor()

    delete_records('..\\src\\sql\\delete_raw_employee_data.sql')

    with open(filepath) as xml_file:
        data_dict = xmltodict.parse(xml_file.read())

    new_list_all = data_dict["EmployeeList"]["Employee"]
    with open('..\\src\\sql\\import_raw_employee_data.sql') as insert_data:
        insert_file_query_xml = "".join(insert_data.readlines())
        cursor.executemany(insert_file_query_xml, new_list_all)
        connection.commit()
    cursor.close()
    connection.close()

if __name__ =="__main__" :
    extract_json_data('..\\data\\employee_2021_08_01.json')
    extract_xml_data('..\\data\\employee_2021_08_01.xml')

