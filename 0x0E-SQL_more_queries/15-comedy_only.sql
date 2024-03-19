-- list all comedy shows in the database 'hbtn_0d_tvshows'
-- result must be sorted in ascending order by the show title
-- only one SELECT statement can be used
SELECT title
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = "Comedy"
GROUP BY title
ORDER BY title;
