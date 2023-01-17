import sqlalchemy
from app.models.database import metadata


plants = sqlalchemy.Table(
    'plants',
    metadata,
    sqlalchemy.Column('plant_id', sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column('name', sqlalchemy.String(30))
)
