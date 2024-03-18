-- update score of 'Bob' in the table in the database of my MySQL server to '10'
-- only allowed to use 'name' field but not 'id' value
UPDATE second_table
SET score = 10
WHERE name = "Bob";
