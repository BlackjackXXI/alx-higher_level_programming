#!/usr/bin/python3
"""
city class definer

"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State
class City(Base):

    """city Class """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
