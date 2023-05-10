from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.config import settings

DATABASE_URI = settings.DATABASE_URI
engine = create_engine(DATABASE_URI)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)
