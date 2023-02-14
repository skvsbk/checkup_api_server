from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.utils import users_crud
from app.models.database import get_db
from app.schemas.user import UserOut
# from app.schemas.user import UserCreate


router = APIRouter()


# @router.get('/', response_model=list[UserOut])
# def get_users(limit: int = 100, skip: int = 0, db: Session = Depends(get_db)):
#     return users_crud.get_all(db=db, limit=limit, skip=skip)


@router.get('/{login}', response_model=UserOut)
def get_user_by_login(login: str, db: Session = Depends(get_db)):
    user = users_crud.get_user_by_login(db=db, login=login)
    print(user)
    if not user:
        raise HTTPException(status_code=200, detail='User not found')
    return user


# @router.post('/', response_model=UserOut)
# def create_user(value: UserCreate, db: Session = Depends(get_db)):
#     db_user = users_crud.get_user_by_login(db=db, login=value.login)
#     if db_user:
#         raise HTTPException(status_code=400, detail='User login already registered')
#     return users_crud.create_user(db=db, user=value)
