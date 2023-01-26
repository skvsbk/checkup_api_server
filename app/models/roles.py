from sqlalchemy import Column, String, Integer
from app.models.database import Base


class RoleDB(Base):
    __tablename__ = 'user_roles'
    role_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50))
