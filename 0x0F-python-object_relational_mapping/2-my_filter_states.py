#!/usr/bin/python3
"""states models"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    db_host = "localhost"
    db_user = sys.argv[1]  # "your_username"
    db_password = sys.argv[2]  # "your_password"
    db_name = sys.argv[3]  # "your_database_name"
    port = 3306
    state_name = sys.argv[4]  # "state name searched"
#     query = "SELECT * FROM `states` WHERE `name` LIKE BINARY\
#  '{}' ORDER BY `id` ASC".format(state_name)
    conn = MySQLdb.connect(
        host=db_host, user=db_user, passwd=db_password,
        db=db_name, port=port, charset="utf8"
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM `states` \
            WHERE BINARY `name` = '{}'".format(state_name))
    [print(state) for state in cur.fetchall()]

    cur.close()
    conn.close()
