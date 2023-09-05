from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    Represents a state in a database table.

    Attributes:
        id (int): An auto-generated, unique integer representing the state's ID. It is also the primary key.
        name (str): A string representing the name of the state. It can't be null and has a maximum length of 128 characters.

    Methods:
        __init__(self, name):
            Initializes a new State instance with the provided name.

        __str__(self):
            Returns a string representation of the State object in the format "State(id=<id>, name='<name>')".

    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"State(id={self.id}, name='{self.name}')"

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    # Replace 'your_username', 'your_password', and 'your_database' with your MySQL credentials.
    DATABASE_URL = 'mysql://your_username:your_password@localhost:3306/your_database'

    # Create the database engine and session
    engine = create_engine(DATABASE_URL, echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create the tables in the database
    Base.metadata.create_all(engine)

    # Close the session
    session.close()
