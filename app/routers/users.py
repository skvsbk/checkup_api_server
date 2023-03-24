from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.utils import users_crud
from app.models.database import get_db
from app.schemas.user import UserOut
# from app.schemas.user import UserCreate


router = APIRouter()


# http://127.0.0.1:8000/users/admin
# {
#   "login": "admin",
#   "name": "admin",
#   "id": 13,
#   "password": "c4c2389238c9a6f75849b",
#   "role_name": "admin"
# }
@router.get('/{login}', response_model=UserOut)
def get_user_by_login(login: str, db: Session = Depends(get_db)):
    user = users_crud.get_user_by_login(db=db, login=login)

    if not user:
        raise HTTPException(status_code=200, detail='User not found')
    return user
