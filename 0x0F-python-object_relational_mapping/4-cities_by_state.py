#!/usr/bin/python3
# Usage: ./4-cities_by_state.py <mysql username> \
#                               <mysql password> \
#                               <database name>
import sys
import MySQLdb

if __name__ == "__main__":
    db_host = "localhost"
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
    port = 3306

    db = MySQLdb.connect(
        host=db_host, user=db_user, passwd=db_password, db=db_name, port=port
    )
    c = db.cursor()
    c.execute("SELECT `c`.`id`, `c`.`name`, `s`.`name` \
                 FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                   ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")
    [print(city) for city in c.fetchall()]

    c.close()
    db.close()
