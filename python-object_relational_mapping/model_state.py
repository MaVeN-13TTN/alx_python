from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
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
