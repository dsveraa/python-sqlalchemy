# import packages from sqlalchemy
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base

# declarate database location
db_url = "sqlite:///database.db"

# create engine
engine = create_engine(db_url)

# create declarative base
Base = declarative_base()

# class to users table
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
       
# create tables
Base.metadata.create_all(engine)
