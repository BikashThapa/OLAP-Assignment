CREATE TABLE dim_department(
							department_id SERIAL,
							department_name VARCHAR(35) NOT NULL,
							CONSTRAINT pk_department_id PRIMARY KEY(department_id)
);