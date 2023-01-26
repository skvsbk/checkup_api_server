from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.models.database import Base
from app.models.roles import RoleDB


class UserDB(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    login = Column(String(10), unique=True)
    password = Column(String(256))
    role_id = Column(Integer, ForeignKey('user_roles.role_id'), index=True)
    name = Column(String(50))
    active = Column(Boolean())

    roles = relationship('RoleDB', backref='users')
