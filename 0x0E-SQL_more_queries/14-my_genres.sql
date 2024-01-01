-- Script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
-- uses a databse to lists all rows in a table corresponding to all rows in another
SELECT g.`name`
FROM `tv_genres` AS g 
INNER JOIN `tv_show_genres` AS s ON g.`id` = s.`genre_id`
INNER JOIN `tv_shows` AS t ON t.`id` = s.`show_id`
WHERE t.`title` = "Dexter"
GROUP BY g.`name`
ORDER BY g.`name` ASC;