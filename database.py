from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os
from dotenv import load_dotenv

load_dotenv(".env")


db_username = os.getenv('DATABASE_USER')
db_password = os.getenv('DATABASE_PASSWORD')
db_host = os.getenv('DATABASE_HOST')
db_port = os.getenv('DATABASE_PORT')
db_name = os.getenv('DATABASE_NAME')

DATABASE_URL = f'postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}'

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()