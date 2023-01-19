from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.models.database import Base


class NfcTagDB(Base):
    __tablename__ = 'nfc_tag'
    nfc_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nfc_serial = Column(String(14))
    plant_id = Column(Integer, ForeignKey('plants.plant_id'), index=True)

    plant = relationship('PlantsDB', backref='nfc_tag')
