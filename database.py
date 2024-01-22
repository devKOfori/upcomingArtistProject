from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase
from data import settings

load_dotenv(".env")

class Base(DeclarativeBase):
    pass

SessionLocal = ""
try:
    print("Initializing Database...")
    engine = create_engine(settings.DATABASE_URL, echo="debug")
    connection = engine.connect()
    print("Connected to database")
    # Base.metadata.create_all(bind=engine)
    # SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    # print("Initializing Database Completed...")
except:
    print("An error occured while connecting to the database")