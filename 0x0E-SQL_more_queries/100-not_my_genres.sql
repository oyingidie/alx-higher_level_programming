-- use the 'hbtn_0d_tvshows' database to list all genres not linked to the show 'Dexter'
-- result must be in ascending order of the genre name
-- maximum of two SELECT statements allowed
SELECT name
FROM tv_genres
WHERE name NOT IN
(
	SELECT name
	FROM tv_genres
	LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
	LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
	WHERE tv_shows.title = "Dexter"
)
GROUP BY name
ORDER BY name;
