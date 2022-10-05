-- listing al records of the second_table of the database
-- using empty string to represent names without a value
SELECT score, name FROM second_table WHERE name != '' ORDER BY score DESC;
