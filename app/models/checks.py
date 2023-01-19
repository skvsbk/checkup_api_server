from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.models.database import Base


class ChecksDB(Base):
    __tablename__ = 'checks'
    check_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    note = Column(String(256))
    checkup_id = Column(Integer, ForeignKey('checkups.checkup_id'), index=True)
    nfc_id = Column(Integer, ForeignKey('nfc_tag.nfc_id'), index=True)

    checkups = relationship('CheckupsDB', backref='checks')
    nfctag = relationship('NfcTagDB', backref='checks')
