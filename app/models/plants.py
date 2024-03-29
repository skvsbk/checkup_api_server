from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.models.database import Base
from app.models.facilities import FacilitiesDB


class PlantsDB(Base):
    __tablename__ = 'plants'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50))
    description_plant = Column(String(150))
    description_params = Column(String(150))
    facility_id = Column(Integer, ForeignKey('facilities.id'), index=True)

    facilities = relationship('FacilitiesDB', backref='plants')
