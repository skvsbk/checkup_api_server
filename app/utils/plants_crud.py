from sqlalchemy.orm import Session
from .base import create_base
from ..schemas.plant import PlantCreate
from ..models import plants


def get_by_facility_id(db: Session, facility_id: int):
    return db.query(plants.PlantsDB).filter(plants.PlantsDB.facility_id == facility_id).all()


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
