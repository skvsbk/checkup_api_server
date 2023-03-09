from sqlalchemy.orm import Session
from app.schemas.user import UserCreate
from app.models import users, roles
from .base import create_base


# def get_all(db: Session, limit: int, skip: int = 0):
#     return db.query(users.UserDB).offset(skip).limit(limit).all()


# http://127.0.0.1:8000/users/admin
def get_user_by_login(db: Session, login: str):
    res = db.query(users.UserDB.id, users.UserDB.login, users.UserDB.name, users.UserDB.password, roles.RoleDB.name.label("role_name")).\
        filter(users.UserDB.login == login, users.UserDB.active == True).join(roles.RoleDB, roles.RoleDB.id == users.UserDB.role_id).first()
    return res


# use for first start (todo make hased passwjrd)
def create_user(db: Session, user: UserCreate):
    # fake_hashed_password = user.password + "notreallyhashed"
    db_user = users.UserDB(login=user.login, password=user.password,
                           role_id=user.role_id, name=user.name, active=user.active)
    create_base(db, db_user)
    return db_user
