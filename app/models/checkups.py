from sqlalchemy import Column, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.models.database import Base
from app.models.routes import RoutesDB
from app.models.users import UserDB


class CheckupsDB(Base):
    __tablename__ = 'checkups'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    completed = Column(Boolean)
    route_id = Column(Integer, ForeignKey('routes.id'), index=True)
    user_id = Column(Integer, ForeignKey('users.id'), index=True)
    t_start = Column(Integer)
    t_end = Column(Integer)

    routes = relationship('RoutesDB', backref='checkups')
    user = relationship('UserDB', backref='checkups')
