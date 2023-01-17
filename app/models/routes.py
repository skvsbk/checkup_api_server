import sqlalchemy
from app.models.database import metadata
# from app.models.checkups import nfc_tag
# from app.models.facilities import facilities


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
