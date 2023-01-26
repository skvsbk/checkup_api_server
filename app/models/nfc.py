from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.models.database import Base
from app.models.plants import PlantsDB


class NfcTagDB(Base):
    __tablename__ = 'nfc_tag'
    nfc_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nfc_serial = Column(String(14))
    plant_id = Column(Integer, ForeignKey('plants.plant_id'), index=True)

    plant = relationship('PlantsDB', backref='nfc_tag')
