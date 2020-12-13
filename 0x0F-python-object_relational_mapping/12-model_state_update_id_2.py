#!/usr/bin/python3
""" script that lists all State objects that contain the letter a
from the database hbtn_0e_6_usa """
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    upd_state = session.query(State).filter(State.id == 2).one()
    upd_state.name = "New Mexico"
    session.commit()
    session.close()
