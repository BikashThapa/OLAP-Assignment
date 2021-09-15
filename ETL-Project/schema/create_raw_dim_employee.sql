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
