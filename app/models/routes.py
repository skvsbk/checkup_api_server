from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.models.database import Base


class RoutesDB(Base):
    __tablename__ = 'routes'
    route_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30))
    facility_id = Column(Integer, ForeignKey('facilities.facility_id'))
    active = Column(Boolean())

    facilities = relationship('FacilitiesDB', backref='routes')