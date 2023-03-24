from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.utils import nfc_crud
from app.models.database import get_db
from app.schemas.nfc import NFCTagCreate, NFCTagOut, NFCTagForPlantOut

router = APIRouter()


@router.get('/', response_model=list[NFCTagOut])
async def get_all_nfc(limit: int = 100, skip: int = 0, db: Session = Depends(get_db)):
    res = nfc_crud.get_all_nfc(db=db, limit=limit, skip=skip)
    if not res:
        raise HTTPException(status_code=200, detail='Plant not found')
    return res


# http://127.0.0.1:8000/nfc/get_plant?nfc_serial=53C5D463200001&facility_id=1
# {
#   "nfc_id": 2,
#   "nfc_active": true,
#   "plant_name": "1.004"
# }
@router.get('/get_plant', response_model=NFCTagForPlantOut)
def get_nfc_for_plant(nfc_serial: str, facility_id: int, db: Session = Depends(get_db)):
    res = nfc_crud.get_nfc_for_plant(db=db, facility_id=facility_id, nfc_serial=nfc_serial)
    if not res:
        raise HTTPException(status_code=200, detail='Plant not found')
    return res


# POST http://127.0.0.1:8000/nfc/?nfc_serial=1234567890&plant_id=23
# {
#   "nfc_serial": "1234567890",
#   "plant_id": 23,
#   "active": true,
#   "id": 21
# }
@router.post('/', response_model=NFCTagOut)
def create_nfc(value: NFCTagCreate, db: Session = Depends(get_db)):
    return nfc_crud.create_nfc(db=db, value=value)
