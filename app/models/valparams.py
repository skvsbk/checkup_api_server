import sqlalchemy
from app.models.database import metadata


val_params = sqlalchemy.Table(
    'val_params',
    metadata,
    sqlalchemy.Column('param_id', sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column('name', sqlalchemy.String(30)),
    sqlalchemy.Column('unit_id', sqlalchemy.ForeignKey('val_units')),
    sqlalchemy.Column('nfc_id', sqlalchemy.ForeignKey('nfc.nfc_id')),
    sqlalchemy.Column('min_value', sqlalchemy.Float),
    sqlalchemy.Column('max_value', sqlalchemy.Float)
)
