from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..utils import checkups_crud
from ..models.database import get_db
from ..schemas.checkup import CheckupOut, CheckupCreate


router = APIRouter()


@router.get('/{checkup_id}', response_model=CheckupOut | None)
async def get_checkup_by_id(checkup_id: int, db: Session = Depends(get_db)):
    return checkups_crud.get_checkup_by_id(db=db, checkup_id=checkup_id)


@router.post('/', response_model=CheckupCreate)
def create_checkup(value: CheckupCreate, db: Session = Depends(get_db)):
    return checkups_crud.create_checkup(db=db, checkup=value)
