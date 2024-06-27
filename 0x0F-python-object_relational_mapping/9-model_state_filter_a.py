#!/usr/bin/python3
"""Lists all State objects that contain the letter 'a' from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create an engine to interact with the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, database))

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query all State objects containing 'a' in their name, sorted by id
    states_with_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    # Print results in the specified format
    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()

