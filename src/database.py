from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from databases import Database
from src.config import settings


DATABASE_URI = settings.DATABASE_URI

engine = create_engine(DATABASE_URI)
database = Database(DATABASE_URI)

Base = declarative_base()
