#!/usr/bin/python3
"""Lists states from the database hbtn_0e_6_usa"""

from sys import argv as a
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=a[1], passwd=a[2], db=a[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states")
    for n in cursor.fetchall():
        print("{}: {}".format(n[0], n[1]))

    cursor.close()
    db.close()
