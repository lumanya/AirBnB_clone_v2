-- Script that prepare a MySQl Server for the project
-- Create Database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create Database User
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev';

-- Grant privileges to datase
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
-- Grant the SELECT privilege to the user hbnb_dev to performance_schema db
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
