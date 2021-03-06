#!/usr/bin/python3
import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

"""Model of state table"""


class State(Base):
    __tablename__ = "states"
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
