from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.utils import roles_crud
from app.models.database import get_db
from app.schemas.role import RoleOut, RoleCreate


router = APIRouter()


@router.get('/', response_model=list[RoleOut])
def get_roles(db: Session = Depends(get_db)): # , limit: int = 100, skip: int = 0):
    return roles_crud.get_all(db=db) # , limit=limit, skip=skip)

# @router.post('/', response_model=RoleOut)
# def create_role(role: RoleCreate, db: Session = Depends(get_db)):
#     return roles_crud.create_role(db=db, role=role)

