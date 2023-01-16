import sqlalchemy
from db.base import metadata


facilities = sqlalchemy.Table(
    'facilities',
    metadata,
    sqlalchemy.Column('facility_id', sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column('name', sqlalchemy.String(30))
)

plants = sqlalchemy.Table(
    'plants',
    metadata,
    sqlalchemy.Column('plant_id', sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column('name', sqlalchemy.String(30))
)
