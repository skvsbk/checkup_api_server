from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.database import get_db
from app.schemas.facility import FacilityOut, FacilityOutAll
from app.utils import facilities_crud

from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

router = APIRouter()


@router.get('/', response_model=list[FacilityOutAll])
async def get_facility(limit: int = 100, skip: int = 0, db: Session = Depends(get_db)):
    # qq = {"response": facilities_crud.get_all(db=db, limit=limit, skip=skip)}
    # return JSONResponse(content=jsonable_encoder(qq))
    return facilities_crud.get_all(db=db, limit=limit, skip=skip)

@router.get('/{facility_name}', response_model=FacilityOut)
async def get_facility_by_name(facility_name: str, db: Session = Depends(get_db)):
    return facilities_crud.get_by_name(db=db, facility_name=facility_name)

# @router.post('/', response_model=FacilityOut)
# def create(value: FacilityCreate, db: Session = Depends(get_db)):
#     return facilities_crud.create(db=db, facility=value)
