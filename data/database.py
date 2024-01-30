from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.declarative import declarative_base
from data import settings

load_dotenv(".env")

class Base(DeclarativeBase):
    pass

SessionLocal = ""
try:
    print("Initializing Database...")
    engine = create_engine(settings.DATABASE_URL, echo="debug")
    Base.metadata.create_all(bind=engine)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    print(SessionLocal)
    print("Initializing Database Completed...")
except:
    print("Error occured")