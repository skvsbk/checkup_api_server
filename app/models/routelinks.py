import sqlalchemy
from app.models.database import metadata


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
