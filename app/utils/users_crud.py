from sqlalchemy.orm import Session
from .base import create_base
from ..schemas.user import UserCreate
from ..models import users


def get_all(db: Session,  limit: int, skip: int = 0):
    return db.query(users.UserDB).offset(skip).limit(limit).all()


def get_user_by_login(db: Session, login: str):
    return db.query(users.UserDB).filter(users.UserDB.login == login).first()


def create_user(db: Session, user: UserCreate):
    # fake_hashed_password = user.password + "notreallyhashed"
    db_user = users.UserDB(login=user.login, password=user.password,
                           role_id=user.role_id, name=user.name, active=user.active)
    create_base(db, db_user)
    return db_user
