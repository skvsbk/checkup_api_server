from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.utils import plants_crud
from app.models.database import get_db
from app.schemas.plant import PlantCreate, PlantOut, PlantByNFCSerialOut


router = APIRouter()

# not sure
@router.get('/facility_id/{facility_id}', response_model=list[PlantOut])
def get_by_facility_id(facility_id: int, db: Session = Depends(get_db)):
    return plants_crud.get_by_facility_id(db=db, facility_id=facility_id)



@router.get('/nfc_serial/{nfc_serial}')
def get_plant_by_nfc_serial( nfc_serial: str, db: Session = Depends(get_db)):
    plant = plants_crud.get_plant_by_nfc_serial(db=db, nfc_serial=nfc_serial)
    if not plant:
        raise HTTPException(status_code=200, detail='Plant not found')
    return plant

@router.get('/facility_id/{facility_id}/plant_name/{plant_name}')
def get_plant_by_name(facility_id: str, plant_name: str, db: Session = Depends(get_db)):
    plant = plants_crud.get_plant_by_name(db=db, facility_id=facility_id, plant_name=plant_name)
    if not plant:
        raise HTTPException(status_code=200, detail='Plant not found')
    return plant


"""
Незанятые помещения
SELECT plants.name FROM `plants`
WHERE plants.facility_id = 1 AND 
NOT EXISTS (SELECT * from nfc_tag WHERE nfc_tag.plant_id = plants.id)
"""

@router.post('/', response_model=PlantOut)
def create_plant(value: PlantCreate, db: Session = Depends(get_db)):
    return plants_crud.create_plant(db=db, plant=value)
