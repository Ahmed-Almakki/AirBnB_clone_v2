/*Write a script that prepares a MySQL server:*/

-- Step 1: Create the database if it does not exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Step 2: Create the user with a password
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Step 3: Grant privileges to the user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Step 4: Flush privileges to apply changes
FLUSH PRIVILEGES;
