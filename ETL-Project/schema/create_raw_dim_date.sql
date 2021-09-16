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