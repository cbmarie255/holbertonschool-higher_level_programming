-- Creating a database and table including auto generation.
-- Database: hbtn_0d_usa; Table: states; id INT unique, auto generated, can’t be null and is a primary key; name VARCHAR(256) can’t be null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256) NOT NULL,
)
AUTO_INCREMENT = 1;
