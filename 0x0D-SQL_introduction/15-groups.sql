-- list the number of records with the same score in table of database in my MySQL server
-- result goes into new column
-- records should be in descending order
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
