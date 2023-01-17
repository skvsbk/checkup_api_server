from databases import Database
from sqlalchemy import create_engine, MetaData
from starlette.config import Config


config = Config('.env')

DATABASE_URL = "mysql+pymysql://root:Ad147852@127.0.0.1:53000/checkup_ogi?charset=utf8mb4" # config('CU_DATABASE_URL', cast=str, default='')

database = Database(DATABASE_URL)
metadata = MetaData()
engine = create_engine(
    DATABASE_URL,
)
