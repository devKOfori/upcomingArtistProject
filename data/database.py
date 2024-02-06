from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase
import settings
from models import Base

load_dotenv(".env")


SessionLocal = None
try:
    print("Initializing Database...")
    engine = create_engine(settings.DATABASE_URL, echo=True)
    Base.metadata.drop_all(bind=engine, checkfirst=False)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    # print(SessionLocal)
    print("Initializing Database Completed...")
except Exception as e:
    print(f"Error occured while connecting to the db: {e}")