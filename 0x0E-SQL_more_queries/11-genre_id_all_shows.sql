-- list all shows contained in the database 'hbtn_0d_tvshows'
-- result must be in ascending order of 'tv_shows.title' & 'tv_show_genres.genre_id'
-- only one SELECT statement can be used
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
