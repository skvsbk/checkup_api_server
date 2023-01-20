from sqlalchemy import Column, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from ..models.database import Base
from ..models.routes import RoutesDB
from ..models.users import UserDB


class CheckupsDB(Base):
    __tablename__ = 'checkups'
    checkup_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    completed = Column(Boolean)
    route_id = Column(Integer, ForeignKey('routes.route_id'), index=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), index=True)
    t_start = Column(Integer)
    t_end = Column(Integer)

    routes = relationship('RoutesDB', backref='checkups')
    user = relationship('UserDB', backref='checkups')
