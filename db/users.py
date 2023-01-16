import sqlalchemy
from db.base import metadata


users = sqlalchemy.Table(
    'users',
    metadata,
    sqlalchemy.Column('user_id', sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column('login', sqlalchemy.String(10)),
    sqlalchemy.Column('password', sqlalchemy.String(256)),
    sqlalchemy.Column('role_id', sqlalchemy.ForeignKey('user_roles.role_id')),
    sqlalchemy.Column('name', sqlalchemy.String(50)),
    sqlalchemy.Column('active', sqlalchemy.Boolean(),
                      server_default=sqlalchemy.sql.expression.true(),
                      nullable=False,)
)

user_roles = sqlalchemy.Table(
    'user_roles',
    metadata,
    sqlalchemy.Column('role_id', sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column('name', sqlalchemy.String(50)),

)
