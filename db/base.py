from databases import Database
from sqlalchemy import create_engine, MetaData

# todo get from .env
DATABASE_URL = '127.0.0.1'
# DATABASE_PORT = 53000
# DATABASE_USER = 'root'
# DATABASE_PASSWORD = 'dkhlkwjdef'
# DATABASE_DB = 'checkup_ogi'

database = Database(DATABASE_URL)
metadata = MetaData()
engine = create_engine(
    DATABASE_URL,
)