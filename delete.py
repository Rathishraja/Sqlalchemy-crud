from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Create an engine to connect to the database
engine = create_engine('sqlite:///mydatabase.db', echo=True)

# Create a base class for declarative models
Base = declarative_base()

# Define a model class representing a table in the database
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

# Create the tables in the database
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

user = User(name='John Doe', email='john@example.com')
session.add(user)
session.commit()

user = User(name='Rathish', email='rathish@example.com')
session.add(user)
session.commit() 

session.delete(user)
session.commit()
