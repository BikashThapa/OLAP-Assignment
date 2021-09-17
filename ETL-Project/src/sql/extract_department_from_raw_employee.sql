INSERT INTO  department (client_department_id ,department_name)
SELECT distinct 
department_id,
department_name
FROM raw_employee;

