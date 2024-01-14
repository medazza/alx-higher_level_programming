#!/usr/bin/python3
"""states models"""
#  Usage: ./0-select_states.py <mysql username> \
#                              <mysql password> \
#                              <database name>

import sys
import MySQLdb

if __name__ == "__main__":
    db_host = "localhost"
    db_user = sys.argv[1]  # "your_username"
    db_password = sys.argv[2]  # "your_password"
    db_name = sys.argv[3]  # "your_database_name"
    port = 3306

    conn = MySQLdb.connect(
        host=db_host, user=db_user, passwd=db_password,
        db=db_name, port=port, charset="utf8"
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM `states` ORDER BY `id` ASC")
    [print(state) for state in cur.fetchall()]
    cur.close()
    conn.close()
