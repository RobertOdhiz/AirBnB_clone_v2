-- Create a database hbnb_test_db that prepares the MySQL server
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Create a new user hbnb_test in localhost
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Grant all privileges to the test user
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
