-- import table dump in a database in my MySQL server
-- display temperature of the top three cities during July and August
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
