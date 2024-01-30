import os
from dotenv import load_dotenv

load_dotenv(".env")


db_username = os.getenv('db_username')
db_password = os.getenv('db_password')
db_host = os.getenv('db_host')
db_port = os.getenv('db_port')
db_name = os.getenv('db_name')

DATABASE_URL = f'postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}'
