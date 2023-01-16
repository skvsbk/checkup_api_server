import sqlalchemy
from db.base import metadata
from db.checkups import checks, nfc_tag


val_units = sqlalchemy.Table(
    'val_units',
    metadata,
    sqlalchemy.Column('unit _id', sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column('name', sqlalchemy.String(10)),
)

val_checks = sqlalchemy.Table(
    'val_checks',
    metadata,
    sqlalchemy.Column('valcheck_id', sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column('value', sqlalchemy.Float),
    sqlalchemy.Column('note', sqlalchemy.String(256)),
    sqlalchemy.Column('param_id', sqlalchemy.ForeignKey('val_params.param_id')),
    sqlalchemy.Column('check_id', sqlalchemy.ForeignKey('checks.check_id'))
)

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