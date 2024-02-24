-- creates and shows grants for users
SELECT id, name FROM cities WHERE ((SELECT id FROM states WHERE ) = state_id) ORDER BY id ASC;
