from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.models.database import Base
from app.models.facilities import FacilitiesDB


class RoutesDB(Base):
    __tablename__ = 'routes'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100))
    facility_id = Column(Integer, ForeignKey('facilities.id'), index=True)
    active = Column(Boolean)

    facilities = relationship('FacilitiesDB', backref='routes')
