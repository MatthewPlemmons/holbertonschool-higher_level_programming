#!/usr/bin/python3
"""Lists states that contain the letter a from the database hbtn_0e_6_usa"""

from sys import argv as a
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


if __name__ == "__main__":
    Session = sessionmaker()
    engine = create_engine("mysql://{}:{}@localhost:3306/{}"
                           .format(a[1], a[2], a[3]))
    Session.configure(bind=engine)
    sess = Session()
    state = State(name="Louisiana")
    sess.add(state)
    sess.commit()
    new_state = sess.query(State).filter_by(name="Louisiana").first()
    print("{}".format(new_state.id))
