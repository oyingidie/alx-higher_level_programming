-- import table dump in a databse in my MySQL server
-- display the maximum temperature of each state in alphabetical order
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
