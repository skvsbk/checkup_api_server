from sqlalchemy import Column, String, Integer
from app.models.database import Base


class ValUnitsDB(Base):
    __tablename__ = 'val_units'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50))
