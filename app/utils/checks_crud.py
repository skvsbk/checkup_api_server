from sqlalchemy.orm import Session
from .base import create_base
from ..schemas.check import CheckCreate
from ..models import checks


def get_by_check_id(db: Session,  check_id: int):
    return db.query(checks.ChecksDB).filter(checks.ChecksDB.check_id == check_id).first()


def create_check(db: Session, check: CheckCreate):
    db_check = checks.ChecksDB(note=check.note, checkip_id=check.checkup_id, nfc_id=check.nfc_id)
    create_base(db, db_check)
    return db_check


def update():
    return


def delete():
    return
