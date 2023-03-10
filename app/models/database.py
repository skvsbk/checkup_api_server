from sqlalchemy import create_engine
from starlette.config import Config
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


config = Config('.env')

DATABASE_URL = "mysql+pymysql://root:Ad147852@127.0.0.1:53000/checkup_ogi?charset=utf8mb4" # config('CU_DATABASE_URL', cast=str, default='')
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
