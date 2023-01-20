from sqlalchemy.orm import Session
from .base import create_base
from ..schemas.nfc import NFCTagCreate
from ..models import nfc


def get_all_nfc(db: Session, limit: int, skip: int = 0):
    return db.query(nfc.NfcTagDB).offset(skip).limit(limit).all()


def create_nfc(db: Session, nfctag: NFCTagCreate):
    db_nfc = nfc.NfcTagDB(nfc_serial=nfctag.nfc_serial, plant_id=nfctag.plant_id)
    create_base(db, db_nfc)
    return db_nfc


# def update():
#     return
#
#
# def delete():
#     return
