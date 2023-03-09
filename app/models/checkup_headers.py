from sqlalchemy import Column, Integer, Boolean, ForeignKey, DateTime, String
from sqlalchemy.orm import relationship
from app.models.database import Base
from app.models.routes import RoutesDB
from app.models.users import UserDB


class CheckupHeadersDB(Base):
    __tablename__ = 'checkup_headers'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, index=True)
    user_name = Column(String(50))
    facility_id = Column(Integer, index=True)
    facility_name = Column(String(30))
    route_id = Column(Integer, index=True)
    route_name = Column(String(30))
    time_start = Column(DateTime)
    time_finish = Column(DateTime)
    is_complete = Column(Boolean)

    