#!/usr/bin/python3
"""
Script that lists all states with a name
starting with N (upper N) from the database
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    connect = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                              passwd=argv[2], db=argv[3], charset="utf8")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    rows = cursor.fetchall()
    for row in rows:
        if row[1].startswith("N"):
            print(row)
    cursor.close()
    connect.close()
