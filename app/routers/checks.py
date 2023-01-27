from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..utils import checks_crud
from ..models.database import get_db
from ..schemas.check import CheckOut, CheckCreate


router = APIRouter()


@router.get('/{check_id}', response_model=CheckOut | None)
def get_by_id(check_id: int, db: Session = Depends(get_db)):
    return checks_crud.get_by_check_id(db=db, check_id=id)


@router.post('/', response_model=CheckOut)
def create_check(value: CheckCreate, db: Session = Depends(get_db)):
    return checks_crud.create_check(db=db, check=value)
