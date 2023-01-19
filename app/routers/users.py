from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.utils import users 
from app.models.database import get_db
from app.schemas.user import UserOut, UserCreate


router = APIRouter()


@router.get('/users', response_model=list[UserOut])
def get_users(db: Session = Depends(get_db)): # , limit: int = 100, skip: int = 0):
    return users.get_all(db=db) # , limit=limit, skip=skip)


@router.post('/users', response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = users.get_user_by_login(db=db, login=user.login)
    if db_user:
        raise HTTPException(status_code=400, detail='User login already registered')
    return users.create_user(db=db, user=user)
