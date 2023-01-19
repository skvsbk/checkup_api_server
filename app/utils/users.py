from app.schemas.user import UserCreate
from sqlalchemy.orm import Session
from app.models import users


def get_all(db: Session):# ,  limit: int, skip: int = 0) -> List[UserOut]:
    return db.query(users.UserDB).offset(0).limit(100).all()


def get_user_by_login(db: Session, login: str):
    res = db.query(users.UserDB).filter(users.UserDB.login == login).first()
    return res


def create_user(db: Session, user: UserCreate):
    # fake_hashed_password = user.password + "notreallyhashed"
    db_user = users.UserDB(login=user.login, password=user.password,
                           role_id=user.role_id, name=user.name, active=user.active)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
