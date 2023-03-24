from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.models.database import Base
from app.models.valunits import ValUnitsDB
from app.models.plants import PlantsDB
from app.models.facilities import FacilitiesDB


class ValParamsDB(Base):
    __tablename__ = 'val_params'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(30))
    facility_id = Column(Integer, ForeignKey('facilities.id'), index=True)
    unit_id = Column(Integer, ForeignKey('val_units.id'), index=True)
    plant_id = Column(Integer, ForeignKey('plants.id'), index=True)
    min_value = Column(Float)
    max_value = Column(Float)

    units = relationship('ValUnitsDB', backref='val_params')
    plants = relationship('PlantsDB', backref='val_params')
    facility = relationship('FacilitiesDB', backref='val_params')
