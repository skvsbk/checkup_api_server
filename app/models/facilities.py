import sqlalchemy
from app.models.database import metadata


facilities = sqlalchemy.Table(
    'facilities',
    metadata,
    sqlalchemy.Column('facility_id', sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column('name', sqlalchemy.String(30))
)
