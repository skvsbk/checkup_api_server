from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..utils import valparams_crud
from ..models.database import get_db
from ..schemas.valparam import ValParamCreate, ValParamOut


router = APIRouter()


@router.get('/{unit_id}') #, response_model=ValParamOut)
async def get_by_unit_id(unit_id: int, db: Session = Depends(get_db)):
    return valparams_crud.get_by_unit_id(db=db, unit_id=unit_id)


@router.post('/', response_model=ValParamOut | None)
def create_param(value: ValParamCreate, db: Session = Depends(get_db)):
    return valparams_crud.create_param(db=db, param=value)

