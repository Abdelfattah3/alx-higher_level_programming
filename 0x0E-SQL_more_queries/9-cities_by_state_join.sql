-- list all the cities
-- creates and shows grants for users
SELECT id, name, (SELECT states.name FROM states WHERE states.id = cities.state_id) AS name FROM cities ORDER BY cities.id ASC;
