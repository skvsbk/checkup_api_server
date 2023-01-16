import sqlalchemy
from db.base import metadata
from db.checkups import nfc_tag
from db.facilities import facilities


routes = sqlalchemy.Table(
    'routes',
    metadata,
    sqlalchemy.Column('route_id', sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column('name', sqlalchemy.String(30)),
    sqlalchemy.Column('plant_id', sqlalchemy.ForeignKey('plants.plant_id')),
    sqlalchemy.Column('active', sqlalchemy.Boolean(),
                      server_default=sqlalchemy.sql.expression.true(),
                      nullable=False,)
)

route_links = sqlalchemy.Table(
    'route_links',
    metadata,
    sqlalchemy.Column('routelink_id', sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column('nfc_id', sqlalchemy.ForeignKey('nfc_tag.nfc_id')),
    sqlalchemy.Column('order', sqlalchemy.Integer),
    sqlalchemy.Column('active', sqlalchemy.Boolean(),
                      server_default=sqlalchemy.sql.expression.true(),
                      nullable=False,)
)
