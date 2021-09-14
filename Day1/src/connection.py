import psycopg2
try:
    connection = psycopg2.connect(user="postgres",
                                password="root2021",
                                host="localhost",
                                port=5432,
                                database="healthCareSystem")
    cursor = connection.cursor()
    
    
    create_dim_date = '''
        CREATE TABLE dim_date(
					date_id SERIAL,
					punch_in_time TIMESTAMP,
					punch_out_time TIMESTAMP,
					punch_apply_date DATE NOT NULL,
					hire_date DATE NOT NULL,
					terminated_date DATE NOT NULL,
					dob DATE NOT NULL,
					CONSTRAINT pk_date_id PRIMARY KEY(date_id)
); 
    '''

  create_dim_department = '''
       CREATE TABLE dim_department(
							department_id SERIAL,
							department_name VARCHAR(35) NOT NULL,
							CONSTRAINT pk_department_id PRIMARY KEY(department_id)
); 
    '''

 create_dim_employee = '''
       CREATE TABLE dim_employee (
                            employee_id SERIAL ,
                            first_name VARCHAR(30) NOT NULL,
                            last_name VARCHAR(30) NOT NULL,
                            location VARCHAR(15) NOT NULL,
                            employee_role VARCHAR(50),
                            manager_role_id NUMERIC(7),
                            cost_center NUMERIC (5) NOT NULL,
                            paycode VARCHAR(7) NOT NULL,
                            CONSTRAINT pk_employee_id PRIMARY KEY(employee_id),
                            
);
 
    '''
 
    
    craete_fact_employee = '''
       CREATE TABLE dim_employee (
                            employee_id SERIAL ,
                            first_name VARCHAR(30) NOT NULL,
                            last_name VARCHAR(30) NOT NULL,
                            location VARCHAR(15) NOT NULL,
                            employee_role VARCHAR(50),
                            manager_role_id NUMERIC(7),
                            cost_center NUMERIC (5) NOT NULL,
                            paycode VARCHAR(7) NOT NULL,
                            CONSTRAINT pk_employee_id PRIMARY KEY(employee_id),
                            
);
 
    '''    
    
    
    cursor.execute(create_dim_department)
    cursor.execute(create_dim_date)  
    cursor.execute(create_dim_employee)  
    cursor.execute(craete_fact_employee)    

    connection.commit()
except Exception as e:
    print("An error has occured", e)
    
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("connection is closed")