from sqlalchemy.orm import Session
from .base import create_base
from app.schemas.nfc import NFCTagCreate
from app.models import nfc


def get_all_nfc(db: Session, limit: int, skip: int = 0):
    return db.query(nfc.NfcTagDB).offset(skip).limit(limit).all()


# def get_plant_by_nfc_serial(db: Session):
#     """
#     SELECT * FROM nfc_tag
#     JOIN plants ON plants.id = nfc_tag.plant_id
#     WHERE nfc_tag.nfc_serial = "53E9DC63200001" AND nfc_tag.active = 1 AND plants.facility_id = 1
#     """



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
