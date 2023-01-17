import sqlalchemy
from app.models.database import metadata


val_units = sqlalchemy.Table(
    'val_units',
    metadata,
    sqlalchemy.Column('unit _id', sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column('name', sqlalchemy.String(10)),
)
