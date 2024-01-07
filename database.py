from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase
import settings

load_dotenv(".env")

class Base(DeclarativeBase):
    pass

def create_db_engine():
    try:
        print("Initializing Database...")
        engine = create_engine(settings.DATABASE_URL, echo="debug")
        Base.metadata.create_all(bind=engine)
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        print("Initializing Database Completed...")
    except:
        print("Error occured")