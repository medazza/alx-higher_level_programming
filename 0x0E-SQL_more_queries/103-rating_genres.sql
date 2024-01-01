-- Scripts that lists all genres in the database hbtn_0d_tvshows_rate by their rating
-- lists all rows in a database linked to a row in another table
SELECT `name`, SUM(r.`rate`) AS `rating`
FROM `tv_genres` AS g
INNER JOIN `tv_show_genres` AS s ON s.`genre_id` = g.`id`
INNER JOIN `tv_show_ratings` AS r ON r.`show_id` = s.`show_id`
GROUP BY `name`
ORDER BY `rating` DESC;