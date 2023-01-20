from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..utils import nfc_crud
from ..models.database import get_db
from ..schemas.nfc import NFCTagCreate, NFCTagOut


router = APIRouter()


@router.get('/', response_model=list[NFCTagOut])
async def get_all_nfc(limit: int = 100, skip: int = 0, db: Session = Depends(get_db)):
    return nfc_crud.get_all_nfc(db=db, limit=limit, skip=skip)


@router.post('/', response_model=NFCTagCreate)
def create_nfc(value: NFCTagCreate, db: Session = Depends(get_db)):
    return nfc_crud.create_nfc(db=db, nfctag=value)
