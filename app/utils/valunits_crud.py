from sqlalchemy.orm import Session
from .base import create_base
from ..schemas.valunit import ValUnitCreate
from ..models import valunits


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
