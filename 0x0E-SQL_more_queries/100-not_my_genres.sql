-- Script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
-- uses a database to list all rows not linked to one row
SELECT DISTINCT `name` FROM `tv_genres` AS g
INNER JOIN `tv_show_genres` AS s ON g.`id` = s.`genre_id`
INNER JOIN `tv_shows` AS t ON s.`show_id` = t.`id`
WHERE g.`name` NOT IN
    (SELECT `name` FROM `tv_genres` AS g
    INNER JOIN `tv_show_genres` AS s ON g.`id` = s.`genre_id`
	INNER JOIN `tv_shows` AS t ON s.`show_id` = t.`id`
	WHERE t.`title` = "Dexter")
GROUP BY g.`name`
ORDER BY g.`name` ASC;