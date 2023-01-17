import sqlalchemy
from app.models.database import metadata


user_roles = sqlalchemy.Table(
    'user_roles',
    metadata,
    sqlalchemy.Column('role_id', sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column('name', sqlalchemy.String(50)),

)
