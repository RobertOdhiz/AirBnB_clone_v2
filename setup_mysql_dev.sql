-- Create a database called hbnb_dev_db in the current MySQL server
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Create the MySQL server user hbnb_dev
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Grants all permissions to the test user hbnb_dev
GRANT ALL ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
