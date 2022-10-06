-- Listing all the cities of Califorinia found on the database.
-- nesting functions!
SELECT id, name FROM hbtn_0d_usa.cities
WHERE hbtn_0d_usa.states.name = Califorina
ORDER BY cities.id ASC
