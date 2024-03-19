-- list all shows contained in 'hbtn_0d_tvshows' without a genre linked
-- result must be in ascending order by 'tv_shows.title' & 'tv_show_genres.genre_id'
-- only one SELECT statement can be used
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id;
