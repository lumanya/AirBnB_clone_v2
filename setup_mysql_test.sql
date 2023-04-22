-- script that prepares as MySQl server for the project:
-- create a database if does not exists
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- create a new user hbnb_test in local host if doesnot exists
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Grant privileges on database hbnb_test_db to hbnb_test
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- Grant SELECT privilege on the databse performance_schema to hbnb_tes user
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
