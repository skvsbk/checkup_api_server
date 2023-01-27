from sqlalchemy import Column, String, Integer
from app.models.database import Base


class FacilitiesDB(Base):
    __tablename__ = 'facilities'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(30))
