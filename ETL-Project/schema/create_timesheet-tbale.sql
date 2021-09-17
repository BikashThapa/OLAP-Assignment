CREATE TABLE timesheet(
id SERIAL,
employee_id VARCHAR(500), 
department_id INTEGER,
shift_start_time TIME,
shift_end_time TIME,
shift_type VARCHAR(100),
hours_woked FLOAT,
attendence VARCHAR(100),
has_taken_break BOOLEAN,
break_hour FLOAT,
was_charge BOOLEAN,
charge_hour FLOAT,
was_on_call BOOLEAN,
on_call_hour FLOAT,
num_teammates_absent SMALLINT,
CONSTRAINT pk_timesheet_id PRIMARY KEY(id),
CONSTRAINT fk_department_id FOREIGN KEY(department_id) REFERENCES department(id)
);

