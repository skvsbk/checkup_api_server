from sqlalchemy import Column, Integer, ForeignKey, DateTime, String, Float
from sqlalchemy.orm import relationship
from app.models.database import Base
from app.models.checkup_headers import CheckupHeadersDB


class CheckupDetailsDB(Base):
    __tablename__ = 'checkup_details'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    header_id = Column(Integer, ForeignKey('checkup_headers.id'), index=True)
    nfc_serial = Column(String(14))
    plant_id = Column(Integer)
    plant_name = Column(String(30))
    val_name = Column(String(30))
    val_min = Column(Float)
    val_max = Column(Float)
    unit_name = Column(String(30))
    val_fact = Column(Float)
    time_check = Column(DateTime)

    checkup_header = relationship('CheckupHeadersDB')
