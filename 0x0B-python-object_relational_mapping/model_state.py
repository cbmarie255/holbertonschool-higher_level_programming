#!/usr/bin/python3
"""
   Modeling models using ORM 
"""
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class State(Base):
    """defining class for State"""
    __tablename__ = 'states'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(128), nullable=False)
