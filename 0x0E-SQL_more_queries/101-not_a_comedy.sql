-- Script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows
-- uses a database to list all rows not linked to one row
SELECT DISTINCT `title` FROM `tv_shows` AS t
LEFT JOIN `tv_show_genres` AS s ON s.`show_id` = t.`id`
LEFT JOIN `tv_genres` AS g ON g.`id` = s.`genre_id`
WHERE t.`title` NOT IN
    (SELECT `title` FROM `tv_shows` AS t
	INNER JOIN `tv_show_genres` AS s ON s.`show_id` = t.`id`
    INNER JOIN `tv_genres` AS g ON g.`id` = s.`genre_id`
	WHERE g.`name` = "Comedy")
GROUP BY `title`
ORDER BY `title` ASC;