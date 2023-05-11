from sqlalchemy import create_engine, MetaData
from databases import Database
from src.config import settings


DATABASE_URI = settings.DATABASE_URI

engine = create_engine(DATABASE_URI)
database = Database(DATABASE_URI)


metadata = MetaData()
