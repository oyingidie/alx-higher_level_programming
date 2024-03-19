-- list all shows contained in 'hbtn_0d_tvshows' that have one linked genre at least
-- result must be in ascending order of 'tvshows.title' & 'tv_shows_genres.genre_id'
-- only one SELECT statement can be used
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_shows_genres.genre_id;
