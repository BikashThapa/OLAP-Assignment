CREATE TABLE fact_employee (
emp_id SERIAL,
employee_id INTEGER ,
department_id INTEGER,
date_id INTEGER ,
salary INTEGER NOT NULL,
fte FLOAT(1) NOT NULL,
hours_worked INTEGER NOT NULL,
CONSTRAINT pk_emp_id PRIMARY KEY(emp_id),
CONSTRAINT fk_employee_id FOREIGN KEY(employee_id) REFERENCES dim_employee(employee_id),
CONSTRAINT fk_department_id FOREIGN KEY(department_id) REFERENCES dim_department(department_id),
CONSTRAINT fk_date_id FOREIGN KEY(date_id) REFERENCES dim_date(date_id),
CONSTRAINT chck_fte CHECK (fte >=0 AND fte <=1)
);
