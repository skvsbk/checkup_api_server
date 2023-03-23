from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.utils import valparams_crud
from app.models.database import get_db
from app.schemas.valparam import ValParamCreate, ValParamOut


router = APIRouter()


# not sure
# @router.get('/{unit_id}') #, response_model=ValParamOut)
# async def get_by_unit_id(unit_id: int, db: Session = Depends(get_db)):
#     return valparams_crud.get_by_unit_id(db=db, unit_id=unit_id)

@router.get('/nfc_serial/{nfc_serial}', response_model=ValParamOut)
async def get_params_by_nfc_serial(nfc_serial: str, db: Session = Depends(get_db)):
    res = valparams_crud.get_params_by_nfc_serial(db=db, nfc_serial=nfc_serial)
    if not res:
        raise HTTPException(status_code=200, detail='Params not found')
    return res


# http://127.0.0.1:8000/valparams/?facility_id=1
# [
#   {
#     "id": 6,
#     "name": "Давление на входе",
#     "min_value": 1,
#     "max_value": 6,
#     "unit_name": "bar"
#   },...
# ]
@router.get('/', response_model=list[ValParamOut])
def get_all_params(facility_id: str, db: Session = Depends(get_db)):
    return valparams_crud.get_all_params(db=db, facility_id=facility_id)

@router.post('/', response_model=ValParamOut | None)
def create_param(value: ValParamCreate, db: Session = Depends(get_db)):
    return valparams_crud.create_param(db=db, param=value)
