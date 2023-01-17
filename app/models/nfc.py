import sqlalchemy
from app.models.database import metadata


nfc_tag = sqlalchemy.Table(
    'nfc_tag',
    metadata,
    sqlalchemy.Column('nfc_id', sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column('nfc_serial', sqlalchemy.String(14)),
    sqlalchemy.Column('plant_id', sqlalchemy.ForeignKey('plants.plant_id'))
)
