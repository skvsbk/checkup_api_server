from sqlalchemy.orm import Session
from app.schemas.valcheck import ValCheckCreate
from app.models import valchecks
from .base import create_base


def get_by_check_id(db: Session, check_id: int):
    return db.query(valchecks.ValChecksDB).filter(valchecks.ValChecksDB.check_id == check_id).first()


def create_valcheck(db: Session, valcheck: ValCheckCreate):
    db_valcheck = valchecks.ValChecksDB(value=valcheck.value, note=valcheck.note,
                                        param_id=valcheck.param_id, check_id=valcheck.check_id)
    create_base(db, db_valcheck)
    return db_valcheck


# def update():
#     return
