from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from ..models.database import Base
from ..models.checkups import CheckupsDB
from ..models.nfc import NfcTagDB

class ChecksDB(Base):
    __tablename__ = 'checks'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    note = Column(String(256))
    checkup_id = Column(Integer, ForeignKey('checkups.id'), index=True)
    nfc_id = Column(Integer, ForeignKey('nfc_tag.id'), index=True)

    checkups = relationship('CheckupsDB', backref='checks')
    nfctag = relationship('NfcTagDB', backref='checks')
