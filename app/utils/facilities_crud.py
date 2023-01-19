from sqlalchemy.orm import Session
from app.schemas.facility import FacilityCreate
from app.models import facilities
from .base import create_base


def get_all(db: Session):
    return db.query(facilities.FacilitiesDB).offset(0).limit(100).all()


def create(db: Session, facility: FacilityCreate):
    db_facility = facilities.FacilitiesDB(name=facility.name)
    # db.add(db_facility)
    # db.commit()
    # db.refresh()
    create_base(db, db_facility)
    return db_facility


def update(db: Session):
    return


def delete(db: Session):
    return
