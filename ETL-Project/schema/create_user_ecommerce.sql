CREATE TABLE IF NOT EXISTS users (
  id SERIAL,
  username VARCHAR(45) NOT NULL,
  email VARCHAR(45) NOT NULL,
  password TEXT NOT NULL,
  PRIMARY KEY (id)
);