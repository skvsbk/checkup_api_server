from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..utils import valchecks_crud
from ..models.database import get_db
from ..schemas.valcheck import ValCheckCreate, ValCheckOut


router = APIRouter()


@router.get('/{id}', response_model=ValCheckOut | None)
def get_by_check_id(check_id: int, db: Session = Depends(get_db)):
    return valchecks_crud.get_by_check_id(db=db, check_id=check_id)


@router.post('/', response_model=ValCheckOut)
def create_user(value: ValCheckCreate, db: Session = Depends(get_db)):
    return valchecks_crud.create_valcheck(db=db, valcheck=value)
