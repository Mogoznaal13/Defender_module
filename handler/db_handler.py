from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

db_name = "sqlite:///handler/coursework.db"
engine = create_engine(db_name)
Base = declarative_base()