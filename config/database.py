import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# The name of the database file
sqlite_file_name = "../database.sqlite"

# Path to the directory containing the database file
base_dir = os.path.dirname(os.path.realpath(__file__))

# Database URL.
database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}"

# Create an engine to connect to the database
engine = create_engine(database_url, echo=True)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)

# Create a base class for all of the tables in the database
Base = declarative_base()