#!/usr/bin/python3
"""states models"""

import sys
import MySQLdb

if __name__ == "__main__":
    db_host = "localhost"
    db_user = sys.argv[1]  # "your_username"
    db_password = sys.argv[2]  # "your_password"
    db_name = sys.argv[3]  # "your_database_name"
    port = 3306
    state_name = sys.argv[4]  # "your_database_name"
    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
    params = (state_name,)
    db = MySQLdb.connect(
        host=db_host, user=db_user, passwd=db_password, db=db_name, port=port
    )
    c = db.cursor()
    c.execute("SELECT *from `states`")
    [print(state) for state in c.fetchall() if state[1] == sys.argv[4]]
