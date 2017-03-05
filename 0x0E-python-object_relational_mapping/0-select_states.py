#!/usr/bin/python3
"""Lists states from the database hbtn_0e_0_usa"""

from sys import argv as a
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=a[1], password=a[2], database=a[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states")
    for n in cursor.fetchall():
        print(n)

    cursor.close()
    db.close()
