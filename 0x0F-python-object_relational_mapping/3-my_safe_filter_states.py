#!/usr/bin/python3
"""Script that does SQL injection"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    connect = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                              passwd=argv[2], db=argv[3], charset="utf8")
    cursor = connect.cursor()
    cursor.execute("""SELECT * FROM states
                   WHERE name = %s ORDER BY states.id ASC""", (argv[4], ))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    connect.close()
