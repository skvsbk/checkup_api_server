import sqlalchemy
from db.base import metadata
from db.facilities import plants
from db.routes import routes


nfc_tag = sqlalchemy.Table(
    'nfc_tag',
    metadata,
    sqlalchemy.Column('nfc_id', sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column('nfc_serial', sqlalchemy.String(14)),
    sqlalchemy.Column('plant_id', sqlalchemy.ForeignKey('plants.plant_id'))
)

checkups = sqlalchemy.Table(
    'checkups',
    metadata,
    sqlalchemy.Column('checkup_id', sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column('completed', sqlalchemy.Boolean),
    sqlalchemy.Column('route_id', sqlalchemy.ForeignKey('routes.route_id')),
    sqlalchemy.Column('t_start', sqlalchemy.Integer),
    sqlalchemy.Column('t_end', sqlalchemy.Integer)
)

checks = sqlalchemy.Table(
    'checks',
    metadata,
    sqlalchemy.Column('check_id', sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column('note', sqlalchemy.String(256)),
    sqlalchemy.Column('checkup_id', sqlalchemy.ForeignKey('checkups.checkup_id')),
    sqlalchemy.Column('nfc_id', sqlalchemy.ForeignKey('nfc_tag.nfc_id')),
)
