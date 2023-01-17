import sqlalchemy
from app.models.database import metadata
# from app.models.facilities import plants
# from app.models.routes import routes


checkups = sqlalchemy.Table(
    'checkups',
    metadata,
    sqlalchemy.Column('checkup_id', sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column('completed', sqlalchemy.Boolean),
    sqlalchemy.Column('route_id', sqlalchemy.ForeignKey('routes.route_id')),
    sqlalchemy.Column('user_id', sqlalchemy.ForeignKey('users.user_id')),
    sqlalchemy.Column('t_start', sqlalchemy.Integer),
    sqlalchemy.Column('t_end', sqlalchemy.Integer)
)
