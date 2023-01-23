from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.database import get_db
from app.schemas.facility import FacilityOut, FacilityCreate
from app.utils import facilities_crud


router = APIRouter()


@router.get('/', response_model=list[FacilityOut])
async def get_facility(limit: int = 100, skip: int = 0, db: Session = Depends(get_db)):
    return facilities_crud.get_all(db=db, limit=limit, skip=skip)


@router.post('/', response_model=FacilityOut)
def create(value: FacilityCreate, db: Session = Depends(get_db)):
    return facilities_crud.create(db=db, facility=value)
