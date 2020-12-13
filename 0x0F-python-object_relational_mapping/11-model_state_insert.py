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
    newbbie = State(name="Louisiana")
    session.add(newbbie)
    session.commit()
    print(newbbie.id)
    session.close()
