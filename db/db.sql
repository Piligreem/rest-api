-- connect to worldskills database
\c worldskills;

 -- clear db 
DROP SCHEMA public CASCADE;
CREATE SCHEMA public;

GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO public;

GRANT pg_read_all_data TO admin_ws;
GRANT pg_write_all_data TO admin_ws;


-- create tables

CREATE TABLE IF NOT EXISTS subdivisions (
  subdivision_id SERIAL PRIMARY KEY,
  title VARCHAR ( 100 ) NOT NULL
);

CREATE TABLE IF NOT EXISTS employees (
  employee_id SERIAL PRIMARY KEY,
  f_name VARCHAR ( 100 ) NOT NULL,
  s_name VARCHAR ( 100 ) NOT NULL,
  surname VARCHAR ( 100 ) NOT NULL,
  subdivision_id INT, 
  FOREIGN KEY (subdivision_id)
      REFERENCES subdivisions (subdivision_id),
  department VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS visitors (
  visitor_id SERIAL PRIMARY KEY,
  f_name VARCHAR ( 50 ) NOT NULL,
  s_name VARCHAR ( 50 ) NOT NULL,
  surname VARCHAR ( 50 ) NOT NULL,
  phone_num VARCHAR(12),
  email VARCHAR ( 50 ) NOT NULL,
  organization VARCHAR ( 50 ),
  notes TEXT,
  birthday DATE NOT NULL,
  passport_data VARCHAR(10) NOT NULL,
  -- visitor_photo BYTEA NOT NULL,
  visitor_photo BYTEA,
  group_id VARCHAR(150),
  -- appointment VARCHAR(50)

);


CREATE TABLE IF NOT EXISTS pass (
  pass_id SERIAL PRIMARY KEY,
  visit_purpose TEXT,
  date_start DATE,
  date_end DATE,
  subdivision_id INT,
  employee_id INT,
  visitor_id INT,
  FOREIGN KEY (subdivision_id)
      REFERENCES subdivisions (subdivision_id),
  FOREIGN KEY (employee_id)
      REFERENCES employees (employee_id),
  FOREIGN KEY (visitor_id)
      REFERENCES visitors (visitor_id)
);


CREATE TABLE IF NOT EXISTS users(
  email VARCHAR(50) PRIMARY KEY,
  password VARCHAR(128) NOT NULL,
  list_requests_id INT[]
);


CREATE TABLE IF NOT EXISTS requests(
  req_id SERIAL PRIMARY KEY,
  req_type VARCHAR(10) NOT NULL,
  subdivision_id INT NOT NULL,
  req_date DATE NOT NULL,
  req_time TIME NOT NULL,
  req_status VARCHAR(20) NOT NULL,
  req_status_description TEXT,
  FOREIGN KEY (subdivision_id)
      REFERENCES subdivisions (subdivision_id),
  user_id VARCHAR(50) NOT NULL,
  FOREIGN KEY (user_id)
      REFERENCES users (email)
);





