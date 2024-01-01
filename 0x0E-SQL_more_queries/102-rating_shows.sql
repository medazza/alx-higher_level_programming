-- Scripts that lists all shows from hbtn_0d_tvshows_rate by their rating
-- lists all rows of a table by the sum of a linked row
SELECT `title`, SUM(r.`rate`) AS `rating`
FROM `tv_shows` AS t
INNER JOIN `tv_show_ratings` AS r ON t.`id` = r.`show_id`
GROUP BY `title`
ORDER BY `rating` DESC;