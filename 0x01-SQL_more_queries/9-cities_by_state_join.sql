-- Lists all cities contained in the database with constraints.
--Each record should display: cities.id - cities.name - states.name;
SELECT cities.id, cities.name, states.name FROM cities 
LEFT JOIN states ON cities.state_id = states.id;
