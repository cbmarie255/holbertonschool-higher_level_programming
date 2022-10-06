-- Creating a database and table including an foreign key.
-- Database: hbtn_0d_usa; Table: cities; state_id INT, can’t be null and must be a FOREIGN KEY that references to id of the states table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id INT AUTO_INCREMENT PRIMARY KEY,
	state_id INT NOT NULL FOREIGN KEY (hbtn_0d_usa.state.id),
	name VARCHAR(256) NOT NULL
)
AUTO_INCREMENT = 1;
