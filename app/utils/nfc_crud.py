from sqlalchemy.orm import Session
from .base import create_base
from app.schemas.nfc import NFCTagCreate
from app.models import nfc, plants


def get_all_nfc(db: Session, limit: int, skip: int = 0):
    return db.query(nfc.NfcTagDB).offset(skip).limit(limit).all()


# def get_plant_by_nfc_serial(db: Session):
#     """
#     SELECT * FROM nfc_tag
#     JOIN plants ON plants.id = nfc_tag.plant_id
#     WHERE nfc_tag.nfc_serial = "53E9DC63200001" AND nfc_tag.active = 1 AND plants.facility_id = 1
#     """



def create_nfc(db: Session, nfc_serial: str, plant_id: int):
    db_nfc = nfc.NfcTagDB(nfc_serial=nfc_serial, plant_id=plant_id, active=True)
    create_base(db, db_nfc)
    return db_nfc




# Check NFC for free (http://127.0.0.1:8000/nfc/get_plant?nfc_serial=53C5D463200001&facility_id=1)
def get_nfc_for_plant(db: Session, nfc_serial: str, facility_id: int):
    """
    SELECT * FROM `plants`
    JOIN nfc_tag ON nfc_tag.plant_id = plants.id
    WHERE plants.facility_id = 1 AND nfc_tag.nfc_serial ="53C5D463200001" AND nfc_tag.active = 1
    """
    res = db.query(nfc.NfcTagDB.id.label("nfc_id"),
                   nfc.NfcTagDB.active.label("nfc_active"),
                   plants.PlantsDB.name.label("plant_name")).\
            join(nfc.NfcTagDB, nfc.NfcTagDB.plant_id == plants.PlantsDB.id).\
            filter(plants.PlantsDB.facility_id == facility_id,
                   nfc.NfcTagDB.nfc_serial == nfc_serial,
                   nfc.NfcTagDB.active == True).first()
    return res

# def update():
#     return
#
#
# def delete():
#     return
