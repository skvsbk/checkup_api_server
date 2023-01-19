from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.utils import roles
from app.models.database import get_db
from app.schemas.role import RoleBase


router = APIRouter()


@router.get('/', response_model=list[RoleBase])
def get_users(db: Session = Depends(get_db)): # , limit: int = 100, skip: int = 0):
    return roles.get_all(db=db) # , limit=limit, skip=skip)
