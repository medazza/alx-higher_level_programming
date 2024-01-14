#!/usr/bin/python3
"""states models
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    db_host = "localhost"
    db_user = sys.argv[1]  # "your_username"
    db_password = sys.argv[2]  # "your_password"
    db_name = sys.argv[3]  # "your_database_name"
    port = 3306
    state_name = sys.argv[4]  # "state name serached"
    # query = "SELECT name FROM cities WHERE state_id = \
    # (SELECT id FROM states WHERE name LIKE BINARY %s) ORDER BY cities.id ASC"
    # params = (state_name,)
    conn = MySQLdb.connect(
        host=db_host, user=db_user, passwd=db_password,
        db=db_name, port=port, charset="utf8"
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                   ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")
    print(", ".join([ct[2] for ct in cur.fetchall() if ct[4] == sys.argv[4]]))

    cur.close()
    conn.close()
