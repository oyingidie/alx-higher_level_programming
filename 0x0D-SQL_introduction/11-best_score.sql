-- list all records with 'score >= 10' in the table of database in MySQL server
-- records should be in descending oreder of 'score'
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
