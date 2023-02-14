from sqlalchemy.orm import Session
from app.models import roles
from app.schemas.role import RoleCreate
from .base import create_base


def get_all(db: Session, limit: int, skip: int = 0):
    return db.query(roles.RoleDB).offset(skip).limit(limit).all()


def create_role(db: Session, role: RoleCreate):
    db_role = roles.RoleDB(role_name=role.role_name)
    create_base(db, db_role)
    return db_role
