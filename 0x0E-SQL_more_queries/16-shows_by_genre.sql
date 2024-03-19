-- list all shows and genres linked to that show from the DB 'hbtn_0d_tvshows'
-- result must be sorted in ascending order of the show title and genre name
-- only one SELECT statement allowed
SELECT title, name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY title, name;
