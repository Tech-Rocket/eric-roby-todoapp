from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# the url is just the location of the db
SQLALCHEMY_DATABASE_URL = "sqlite:///./todosapp.db"


# after creating the url, you need to import
# create_engine from sqlalchemy, and write a variable
# and assign the SQLALCHEMY_DATABASE_URL to it

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)


# next you create the SessionLocal by importing
# the sessionmaker from sqlalchemy.orm
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# finally you need to create an object of the database
# that you can import in another file
Base = declarative_base()
