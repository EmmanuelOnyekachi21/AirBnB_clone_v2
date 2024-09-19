-- Create the database if it does not exist
CREATE DATABASE IF NOT EXISTS `{{DB_NAME}}`;

-- Create the user with a specified password if it does not exist
CREATE USER IF NOT EXISTS '{{DB_USER}}'@'localhost' IDENTIFIED BY '{{DB_PASSWORD}}';

-- Grant all privileges on the database to the user
GRANT ALL PRIVILEGES ON `{{DB_NAME}}`.* TO '{{DB_USER}}'@'localhost';

-- Grant SELECT privilege on the performance_schema database to the user
GRANT SELECT ON performance_schema.* TO '{{DB_USER}}'@'localhost';

-- Apply the changes
FLUSH PRIVILEGES;