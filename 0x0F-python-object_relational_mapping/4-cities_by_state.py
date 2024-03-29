#!/usr/bin/python3
"""states models"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    db_host = "localhost"
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
    port = 3306

    conn = MySQLdb.connect(
        host=db_host, user=db_user, passwd=db_password,
        db=db_name, port=port, charset="utf8"
    )
    cur = conn.cursor()

    cur.execute("SELECT `c`.`id`, `c`.`name`, `s`.`name` \
                 FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                   ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")
    [print(city) for city in cur.fetchall()]
    cur.close()
    conn.close()
