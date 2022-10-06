-- Creating a new database and new user with select privileges and a password.
-- Database: hbtn_0d_2; User: user_0d_2; Password: user_0d_2_pwd;
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost'
IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2 . * TO 'user_0d_2'@'localhost';
