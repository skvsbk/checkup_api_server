import os

from sqlalchemy import create_engine
# from starlette.config import Config
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv, find_dotenv


# config = Config('.env_db')

# DATABASE_URL = "mysql+pymysql://root:Ad147852@db:53000/checkup_ogi?charset=utf8mb4" # config('CU_DATABASE_URL', cast=str, default='')
load_dotenv(find_dotenv('./.env_db'))
DATABASE_URL = os.getenv('DATABASE_URL')
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
