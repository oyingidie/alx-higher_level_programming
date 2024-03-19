-- list all cities contained in the database 'hbtn_0d_usa'
-- result should be in ascending order of 'cities.id'
-- only one SELECT statement can be used
SELECT cities.id, cities.name, states.name
FROM cities LEFT JOIN states ON states.id = cities.state_id
ORDER BY cities.id;
