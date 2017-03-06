#!/usr/bin/python3
"""List cities from database."""

from sys import argv as a
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=a[1], passwd=a[2], db=a[3])
    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities JOIN states \
    ON cities.state_id = states.id WHERE states.name = %s", (a[4],))
    print(', '.join(n[0] for n in cursor.fetchall()))

    cursor.close()
    db.close()
