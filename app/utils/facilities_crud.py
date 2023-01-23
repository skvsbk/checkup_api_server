from sqlalchemy.orm import Session
from app.schemas.facility import FacilityCreate
from app.models import facilities
from .base import create_base


def get_all(db: Session, limit: int, skip: int = 0):
    return db.query(facilities.FacilitiesDB).offset(skip).limit(limit).all()


def create(db: Session, facility: FacilityCreate):
    db_facility = facilities.FacilitiesDB(name=facility.name)
    create_base(db, db_facility)
    return db_facility


# def update(db: Session):
#     return
#
#
# def delete(db: Session):
#     return
