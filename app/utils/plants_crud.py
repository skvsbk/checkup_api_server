from sqlalchemy.orm import Session
from sqlalchemy import or_
from app.schemas.plant import PlantCreate
from app.models import plants, nfc, facilities
from .base import create_base


# for listView (http://127.0.0.1:8000/plants/?facility_id=1)
def get_plants_by_facility_id(db: Session, facility_id: int):
    """
    SELECT * FROM plants
    JOIN nfc_tag ON nfc_tag.plant_id = plants.id
    WHERE plants.facility_id = 1
    """
    res = db.query(plants.PlantsDB.name.label("plant_name"), nfc.NfcTagDB.nfc_serial.label("nfc_serial"),
                   nfc.NfcTagDB.active.label("active")). \
        outerjoin(nfc.NfcTagDB, nfc.NfcTagDB.plant_id == plants.PlantsDB.id). \
        filter(plants.PlantsDB.facility_id == facility_id).order_by(plants.PlantsDB.name).all()
    return res


def get_plant_by_nfc_serial(db: Session, nfc_serial: str):
    """
    SELECT plants.name, plants.description_plant, plants.description_params, facilities.name FROM plants
    JOIN nfc_tag ON plants.id = nfc_tag.plant_id
    JOIN facilities ON plants.facility_id = facilities.id
    WHERE nfc_tag.nfc_serial = "53E9DC63200001" AND nfc_tag.active = 1
    """
    # todo: add facility_id from request
    return db.query(plants.PlantsDB.name.label('plant_name'),
                    plants.PlantsDB.description_plant.label('description_plant'),
                    plants.PlantsDB.description_params.label('description_params'),
                    facilities.FacilitiesDB.name.label('facility_name')). \
        join(nfc.NfcTagDB, nfc.NfcTagDB.plant_id == plants.PlantsDB.id). \
        join(facilities.FacilitiesDB, facilities.FacilitiesDB.id == plants.PlantsDB.facility_id). \
        filter(nfc.NfcTagDB.nfc_serial == nfc_serial). \
        filter(nfc.NfcTagDB.active == 1).first()


# check unique name (http://127.0.0.1:8000/plants/1.004?facility_id=1)
def get_plant_by_name(db: Session, plant_name: str, facility_id: int):
    """
    SELECT * from plants
    WHERE plants.name = '1.004'
    AND plants.facility_id = 1
    """
    res = db.query(plants.PlantsDB). \
        filter(plants.PlantsDB.name == plant_name). \
        filter(plants.PlantsDB.facility_id == facility_id).first()
    return res


# save to DB (http://127.0.0.1:8000/plants/?plant_name=1.012&facility_id=1)
def create_plant(db: Session, plant: PlantCreate):
    db_plant = plants.PlantsDB(name=plant.name,
                               facility_id=plant.facility_id,
                               description_plant=plant.description_plant,
                               description_params=plant.description_params
                               )
    create_base(db, db_plant)
    return db_plant


# Get free plants http://127.0.0.1:8000/plants/free?facility_id=1
def get_plant_for_free(db: Session, facility_id: str):
    """
    Free plants (a new one and if nfc.active is false)
    SELECT * from plants
    LEFT JOIN nfc_tag ON nfc_tag.plant_id = plants.id
    WHERE plants.facility_id = 1 AND (nfc_tag.id IS NULL OR nfc_tag.active = 0)
    """
    res = db.query(plants.PlantsDB.id, plants.PlantsDB.name, nfc.NfcTagDB.nfc_serial). \
        outerjoin(nfc.NfcTagDB, nfc.NfcTagDB.plant_id == plants.PlantsDB.id). \
        filter(plants.PlantsDB.facility_id == facility_id).filter(
        or_(nfc.NfcTagDB.id == None, nfc.NfcTagDB.active == False)). \
        order_by(plants.PlantsDB.name).all()
    return res
