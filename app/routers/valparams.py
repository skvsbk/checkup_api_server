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

@router.get('/nfc_serial/{nfc_serial}')
async def get_params_by_nfc_serial(nfc_serial: str, db: Session = Depends(get_db)):
    params = valparams_crud.get_params_by_nfc_serial(db=db, nfc_serial=nfc_serial)
    if not params:
        raise HTTPException(status_code=200, detail='Params not found')
    return params

@router.post('/', response_model=ValParamOut | None)
def create_param(value: ValParamCreate, db: Session = Depends(get_db)):
    return valparams_crud.create_param(db=db, param=value)
