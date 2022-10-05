-- creating a table with given parameters
-- table example
CREATE TABLE IF NOT EXISTS second_table (
	id int,
	name VARCHAR(256),
	score int
);
INSERT INTO second_table(id, name, score)
VALUES('1', 'John', '10');
INSERT INTO second_table(id, name, score)
VALUES('2', 'Alex', '3');
INSERT INTO second_table(id, name, score)
VALUES('3', 'Bob', '14');
INSERT INTO second_table(id, name, score)
VALUES('4', 'George', '8');
