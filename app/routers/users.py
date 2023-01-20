from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..utils import users_crud
from ..models.database import get_db
from ..schemas.user import UserOut, UserCreate


router = APIRouter()


@router.get('/', response_model=list[UserOut])
def get_users(db: Session = Depends(get_db), limit: int = 100, skip: int = 0):
    return users_crud.get_all(db=db, limit=limit, skip=skip)


@router.get('/{login}', response_model=UserOut)
def get_user_by_login(login: str, db: Session = Depends(get_db)): # , limit: int = 100, skip: int = 0):
    return users_crud.get_user_by_login(db=db, login=login) # , limit=limit, skip=skip)


@router.post('/', response_model=UserOut)
def create_user(value: UserCreate, db: Session = Depends(get_db)):
    db_user = users_crud.get_user_by_login(db=db, login=value.login)
    if db_user:
        raise HTTPException(status_code=400, detail='User login already registered')
    return users_crud.create_user(db=db, user=value)
