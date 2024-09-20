-- A script that prepares a MySQL server for the project.
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create the user if it doesn't exist and set the password
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges on the database hbnb_dev_db to the user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT privilege on the database performance_schema to the User
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Flush Privileges to ensure that all changes take effect
FLUSH PRIVILEGES;
