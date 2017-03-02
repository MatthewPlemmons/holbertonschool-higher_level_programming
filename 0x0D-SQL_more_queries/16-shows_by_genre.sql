-- List all shows and genres lined to that show.
SELECT tv_shows.title, tv_genres.name FROM tv_show_genres
RIGHT OUTER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
RIGHT OUTER JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC;
