-- list all cities of California found in the database 'hbtn_0d_usa'
-- result should be in ascending order of 'cities.id'
SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = "California")
ORDER BY id;
