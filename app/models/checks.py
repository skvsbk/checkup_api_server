from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.models.database import Base
from app.models.checkups import CheckupsDB
from app.models.nfc import NfcTagDB

class ChecksDB(Base):
    __tablename__ = 'checks'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    checkup_id = Column(Integer, ForeignKey('checkups.id'), index=True)
    nfc_id = Column(Integer, ForeignKey('nfc_tag.id'), index=True)
    t_check = Column(DateTime)

    checkups = relationship('CheckupsDB', backref='checks')
    nfctag = relationship('NfcTagDB', backref='checks')
