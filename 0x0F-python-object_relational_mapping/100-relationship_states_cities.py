#!/usr/bin/python3
"""model state
"""
from sqlalchemy import create_engine
from relationship_city import City
from relationship_state import State, Base
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    newState = State(name='California')
    newCity = City(name='San Francisco', state=newState)
    ## newState.cities.append(newCity)
    session.add([newState, newCity])
    session.commit()
    session.close()
