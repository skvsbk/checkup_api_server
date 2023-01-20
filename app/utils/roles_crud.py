from sqlalchemy.orm import Session
from .base import create_base
from ..models import roles
from ..schemas.role import RoleCreate


def get_all(db: Session, limit: int, skip: int = 0):
    return db.query(roles.RoleDB).offset(skip).limit(limit).all()


def create_role(db: Session, role: RoleCreate):
    db_role = roles.RoleDB(name=role.name)
    create_base(db, db_role)
    return db_role
