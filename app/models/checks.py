import sqlalchemy
from app.models.database import metadata


checks = sqlalchemy.Table(
    'checks',
    metadata,
    sqlalchemy.Column('check_id', sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column('note', sqlalchemy.String(256)),
    sqlalchemy.Column('checkup_id', sqlalchemy.ForeignKey('checkups.checkup_id')),
    sqlalchemy.Column('nfc_id', sqlalchemy.ForeignKey('nfc_tag.nfc_id')),
)
