from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.models.database import Base
from app.models.valunits import ValUnitsDB
from app.models.nfc import NfcTagDB


class ValParamsDB(Base):
    __tablename__ = 'val_params'

    param_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(30))
    unit_id = Column(Integer, ForeignKey('val_units.unit_id'), index=True)
    nfc_id = Column(Integer, ForeignKey('nfc_tag.nfc_id'), index=True)
    min_value = Column(Float)
    max_value = Column(Float)

    units = relationship('ValUnitsDB', backref='val_params')
    nfctag = relationship('NfcTagDB', backref='val_params')
