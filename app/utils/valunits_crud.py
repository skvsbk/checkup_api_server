from sqlalchemy.orm import Session
from app.schemas.valunit import ValUnitCreate
from app.models import valunits
from .base import create_base


def get_all_units(db: Session, limit: int, skip: int = 0):
    return db.query(valunits.ValUnitsDB).offset(skip).limit(limit).all()


def create_unit(db: Session, unit: ValUnitCreate):
    db_unit = valunits.ValUnitsDB(name=unit.name)
    create_base(db, db_unit)
    return db_unit


# def update():
#     return
#
#
# def delete():
#     return
