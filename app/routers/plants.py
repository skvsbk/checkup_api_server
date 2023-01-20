from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..utils import plants_crud
from ..models.database import get_db
from ..schemas.plant import PlantCreate, PlantOut


router = APIRouter()


@router.get('/{facility_id}', response_model=list[PlantOut])
def get_by_facility_id(facility_id: int, db: Session = Depends(get_db)):
    return plants_crud.get_by_facility_id(db=db, facility_id=facility_id)


@router.post('/', response_model=PlantOut)
def create_plant(value: PlantCreate, db: Session = Depends(get_db)):
    return plants_crud.create_plant(db=db, plant=value)
