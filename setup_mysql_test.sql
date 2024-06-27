/*Write a script that prepares a MySQL server for the project:*/

-- step1: create database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- step2: create new user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- step3: GRANT PRIVILEGS
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
