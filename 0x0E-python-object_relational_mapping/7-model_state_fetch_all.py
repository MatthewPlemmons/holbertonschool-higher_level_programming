#!/usr/bin/python3
"""Lists states from the database hbtn_0e_6_usa"""

from sys import argv as a
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine("mysql://{}:{}@localhost:3306/{}"
                           .format(a[1], a[2], a[3]))
    states = engine.execute("SELECT * FROM states")
    for n in states:
        print("{}: {}".format(n[0], n[1]))
