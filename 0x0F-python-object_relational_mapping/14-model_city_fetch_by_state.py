#!/usr/bin/python3
""" prints the State object with the name passed as argument from the database
"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for rows in (session.query(State.name, City.id, City.name)
                 .filter(State.id == City.state_id)):
        print(rows[0] + ": (" + str(rows[1]) + ") " + rows[2])
    session.close()
