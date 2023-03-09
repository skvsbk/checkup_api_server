from sqlalchemy.orm import Session
from app.schemas.facility import FacilityCreate
from app.models import facilities
from .base import create_base


# http://127.0.0.1:8000/facilities/?limit=100&skip=0
def get_all(db: Session, limit: int, skip: int = 0):
    return db.query(facilities.FacilitiesDB.name).offset(skip).limit(limit).all()


# http://127.0.0.1:8000/facilities/%D0%9F%D1%83%D1%88%D0%BA%D0%B8%D0%BD
def get_facility_by_name(db: Session, facility_name: str):
    return db.query(facilities.FacilitiesDB).filter(facilities.FacilitiesDB.name == facility_name).first()

# def create(db: Session, facility: FacilityCreate):
#     db_facility = facilities.FacilitiesDB(name=facility.name)
#     create_base(db, db_facility)
#     return db_facility


# def update(db: Session):
#     return
#
#
# def delete(db: Session):
#     return
