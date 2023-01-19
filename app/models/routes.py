from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from app.models.database import Base


class RoutesDB(Base):
    __tablename__ = 'routes'
    route_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30))
    plant_id = Column(Integer, ForeignKey('plants.plant_id'))
    active = Column(Boolean())