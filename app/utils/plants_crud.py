from sqlalchemy.orm import Session
from app.schemas.plant import PlantCreate
from app.models import plants, nfc, facilities
from .base import create_base


def get_by_facility_id(db: Session, facility_id: int):
    return db.query(plants.PlantsDB).filter(plants.PlantsDB.facility_id == facility_id).all()

def get_plant_by_name(db: Session, facility_id: str, plant_name: str):
    return db.query(plants.PlantsDB).\
        filter(plants.PlantsDB.name == plant_name).\
        filter(plants.PlantsDB.facility_id == facility_id).first()

def get_plant_by_nfc_serial(db: Session, nfc_serial: str):
    """
    SELECT plants.name, facilities.name FROM plants
    JOIN nfc_tag ON plants.id = nfc_tag.plant_id
    JOIN facilities ON plants.facility_id = facilities.id
    WHERE nfc_tag.nfc_serial = "53E9DC63200001" AND nfc_tag.active = 1
    """
    # todo: add facility_id from request
    return db.query(plants.PlantsDB.name, facilities.FacilitiesDB.name.label('facility')).\
        join(nfc.NfcTagDB, nfc.NfcTagDB.plant_id == plants.PlantsDB.id).\
        join(facilities.FacilitiesDB, facilities.FacilitiesDB.id == plants.PlantsDB.facility_id).\
        filter(nfc.NfcTagDB.nfc_serial == nfc_serial).\
        filter(nfc.NfcTagDB.active == 1).first()


def create_plant(db: Session, plant: PlantCreate):
    db_plant = plants.PlantsDB(name=plant.name, facility_id=plant.facility_id)
    create_base(db, db_plant)
    return db_plant


# def update():
#     return
#
#
# def delete():
#     return
