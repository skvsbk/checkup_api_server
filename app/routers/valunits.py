from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.utils import valunits_crud
from app.models.database import get_db
from app.schemas.valunit import ValUnitCreate, ValUnitOut


router = APIRouter()


@router.get('/', response_model=list[ValUnitOut])
def get_users(limit: int = 100, skip: int = 0, db: Session = Depends(get_db)):
    return valunits_crud.get_all_units(db=db, limit=limit, skip=skip)


@router.post('/', response_model=ValUnitOut | None)
def create_unit(value: ValUnitCreate, db: Session = Depends(get_db)):
    return valunits_crud.create_unit(db=db, unit=value)
