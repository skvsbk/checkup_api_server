import sqlalchemy
from app.models.database import metadata


val_checks = sqlalchemy.Table(
    'val_checks',
    metadata,
    sqlalchemy.Column('valcheck_id', sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column('value', sqlalchemy.Float),
    sqlalchemy.Column('note', sqlalchemy.String(256)),
    sqlalchemy.Column('param_id', sqlalchemy.ForeignKey('val_params.param_id')),
    sqlalchemy.Column('check_id', sqlalchemy.ForeignKey('checks.check_id'))
)
