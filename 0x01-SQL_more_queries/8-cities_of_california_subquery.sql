-- Listing all the cities of Califorinia found on the database.
-- nesting functions!
SELECT id, name FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY cities.id ASC;
