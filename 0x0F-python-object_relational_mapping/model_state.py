#!/usr/bin/python3
"""Defines the State class and an instance of Base"""
import sys
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

# Create an instance of declarative_base
Base = declarative_base()

class State(Base):
    """State class that inherits from Base"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    # Create a connection to the database specified in command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, database), pool_pre_ping=True)
    
    # Create all tables in the database (if they do not exist)
    Base.metadata.create_all(engine)

