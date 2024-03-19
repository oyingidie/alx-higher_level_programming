-- use the 'hbtn_0d_tvshows' databse to list all genres of the show 'Dexter'
-- records must be sorted in ascending order of the genre name
-- only one SELECT statement can be used
SELECT name
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = "Dexter"
GROUP BY name
ORDER BY name;
