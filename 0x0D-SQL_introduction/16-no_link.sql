-- list all records of the table of database in my MySQL server
-- rows must have a value for 'name'
-- records should be in descending order of 'score'
SELECT score, name
FROM second_table
WHERE name != ""
ORDER BY score DESC;
