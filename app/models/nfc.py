from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.models.database import Base
from app.models.plants import PlantsDB


class NfcTagDB(Base):
    __tablename__ = 'nfc_tag'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nfc_serial = Column(String(14))
    plant_id = Column(Integer, ForeignKey('plants.id'), index=True)
    active = Column(Boolean)

    plant = relationship('PlantsDB', backref='nfc_tag')
