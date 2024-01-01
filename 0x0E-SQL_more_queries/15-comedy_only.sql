-- Script that lists all Comedy shows in the database hbtn_0d_tvshows
-- lists all rows of a database corresponding to a column value
SELECT t.`title` FROM `tv_shows` AS t
INNER JOIN `tv_show_genres` AS s ON t.`id` = s.`show_id`
INNER JOIN `tv_genres` AS g ON g.`id` = s.`genre_id`
WHERE g.`name` = "Comedy"
GROUP BY t.`title`
ORDER BY t.`title` ASC;