from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

"""Model of state table"""

Base = declarative_base()

class State(Base):
    __tablename__ = "states"
    id = Column(Integer, unique=True, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
