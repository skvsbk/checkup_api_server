from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.utils import plants_crud
from app.models.database import get_db
from app.schemas.plant import PlantCreate, PlantOut, PlantByNFCSerialOut, PlantByFacilityIdOut, PlantForFreeOut


router = APIRouter()


# for listView (http://127.0.0.1:8000/plants/?facility_id=1)
# [
#   {
#     "plant_name": "1.004",
#     "nfc_serial": "53C5D463200001",
#     "active": true
#   },
#   {
#     "plant_name": "1.006",
#     "nfc_serial": "53B6CF63200001",
#     "active": true
#   },....
# ]
# @router.get('/facility_id/{facility_id}', response_model=list[PlantOut])
@router.get('/', response_model=list[PlantByFacilityIdOut])
def get_plants_by_facility_id(facility_id: int, db: Session = Depends(get_db)):
    res = plants_crud.get_plants_by_facility_id(db=db, facility_id=facility_id)
    # if not plants:
    #     raise HTTPException(status_code=200, detail='Plants not found')

    return res


@router.get('/nfc_serial/{nfc_serial}', response_model=PlantByNFCSerialOut)
def get_plant_by_nfc_serial(nfc_serial: str, db: Session = Depends(get_db)):
    plant = plants_crud.get_plant_by_nfc_serial(db=db, nfc_serial=nfc_serial)
    if not plant:
        raise HTTPException(status_code=200, detail='Plant not found')
    return plant


# check unique name (http://127.0.0.1:8000/plants/name/1.004?facility_id=1)
# {
#   "facility_id": 1,
#   "name": "1.004",
#   "id": 3
# }
@router.get('/name/{plant_name}', response_model=PlantOut)
def get_plant_by_name(plant_name: str, facility_id: int, db: Session = Depends(get_db)):
    plant = plants_crud.get_plant_by_name(db=db, plant_name=plant_name, facility_id=facility_id)
    if not plant:
        raise HTTPException(status_code=200, detail='Plant not found')
    return plant


# Get free plants http://127.0.0.1:8000/plants/free?facility_id=1
# [
#   {
#     "id": 31,
#     "name": "1.012",
#     "nfc_serial": null
#   },
#   {
#     "id": 8,
#     "name": "2.017",
#     "nfc_serial": "53E9DC63200001"
#   },...
# ]
@router.get('/free', response_model=list[PlantForFreeOut])
def get_plant_for_free(facility_id: str, db: Session = Depends(get_db)):
    plants = plants_crud.get_plant_for_free(db=db, facility_id=facility_id)
    return plants


# save to DB (POST http://127.0.0.1:8000/plants/?plant_name=1.012&facility_id=1)
# {
#   "name": "1.012",
#   "facility_id": 1,
#   "id": 31
# }
@router.post('/')
def create_plant(value: PlantCreate,  db: Session = Depends(get_db)):
    return plants_crud.create_plant(db=db, plant=value)
