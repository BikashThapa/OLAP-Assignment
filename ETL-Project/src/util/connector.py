import psycopg2

def connect():
    return psycopg2.connect(user="postgres",
                                password="root2021",
                                host="localhost",
                                port=5432,
                                database="healthCareSystem")

def connect1():
    return psycopg2.connect(user="postgres",
                                password="root2021",
                                host="localhost",
                                port=5432,
                                database="testEcommercce")


def delete_records(file_path):
    connection = connect()
    cursor = connection.cursor()
    with open(file_path) as delete_data:
        delete_all = "".join(delete_data.readlines())
        cursor.execute(delete_all)
        connection.commit()
    cursor.close()
    connection.close()
