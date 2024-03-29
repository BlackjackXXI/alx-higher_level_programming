#!/usr/bin/python3
"""
a Python file similar to model_state.py named model_city.py that contains the class definition of a City

"""
from sys import argv
from model_state import Base, State
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_city import City
if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = Session(engine)

    locations = session.query(City, State).filter(
        City.state_id == State.id).order_by(City.id).all()
    
    for city, state in locations:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
