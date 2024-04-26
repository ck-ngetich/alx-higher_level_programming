#!/usr/bin/python3
"""
Script that takes the name of a state as argument
and list all the cities of that state
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    connect = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                              passwd=argv[2], db=argv[3], charset="utf8")
    cursor = connect.cursor()
    cursor.execute("""
        SELECT cities.name FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        """, (argv[4], ))
    print(", ".join(map(lambda x: x[0], cursor.fetchall())))
    cursor.close()
    connect.close()
