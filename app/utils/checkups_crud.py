from sqlalchemy.orm import Session
from .base import create_base
from ..schemas.checkup import CheckupCreate
from ..models import checkups


def get_checkup_by_id(db: Session,  checkup_id: int):
    return db.query(checkups.CheckupsDB).filter(checkups.CheckupsDB.id == checkup_id).first()


def create_checkup(db: Session, checkup: CheckupCreate):
    db_checkup = checkups.CheckupsDB(completed=checkup.completed,
                                     route_id=checkup.route_id, user_id=checkup.user_id,
                                     t_start=checkup.t_start, t_end=checkup.t_end)
    create_base(db, db_checkup)
    return db_checkup


# def update():
#     return
#
#
# def delete():
#     return
def create_checkup_by_user_id(db, checkup_header):
    return None