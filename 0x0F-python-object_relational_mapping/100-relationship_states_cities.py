#!/usr/bin/python3
"""Create a State with a linked City in the database hbtn_0e_100_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create an engine to interact with the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, database))

    # Bind the Base class to the engine
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Create a new State
    california = State(name="California")

    # Create a new City linked to the State
    san_francisco = City(name="San Francisco", state=california)

    # Add the new State and City to the session
    session.add(california)
    session.add(san_francisco)

    # Commit the changes to the database
    session.commit()

    # Print the new state id
    print(california.id)

    # Close the session
    session.close()

