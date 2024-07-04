#!/usr/bin/python3
"""Define the State class"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import Base

class State(Base):
    """State class that inherits from Base"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(256), nullable=False)
    cities = relationship("City", cascade="all, delete-orphan", back_populates="state")

