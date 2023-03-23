from sqlalchemy.orm import Session
from sqlalchemy import desc
from .base import create_base
from app.schemas.checkup_header import CheckupHeaderCreate, CheckupHeaderUpdate
from app.models import checkup_headers



def get_checkup_by_user_id(db: Session,  user_id: int):
    res = db.query(checkup_headers.CheckupHeadersDB).filter(checkup_headers.CheckupHeadersDB.user_id == user_id).all()
    return res


def get_last_checkup_by_user_id(db: Session,  user_id: int, limit: int):
    """
    SELECT * FROM checkup_headers
    WHERE checkup_headers.user_id = 18
    ORDER BY checkup_headers.time_start DESC
    LIMIT 10
    """
    return db.query(checkup_headers.CheckupHeadersDB).\
        filter(checkup_headers.CheckupHeadersDB.user_id == user_id).\
        order_by(desc(checkup_headers.CheckupHeadersDB.time_start)).limit(limit).all()

def get_total_checkup_by_user_id(db: Session, user_id: int):
    """
    SELECT COUNT(checkup_headers.id) AS total FROM checkup_headers
    WHERE checkup_headers.user_id = 18
    """
    return db.query(checkup_headers.CheckupHeadersDB.id).\
        filter(checkup_headers.CheckupHeadersDB.user_id == user_id).count()


def get_done_or_not_checkup_by_user_id(db: Session, user_id: int, is_complete: bool):
    """
    SELECT COUNT(checkup_headers.id) AS total FROM checkup_headers
    WHERE checkup_headers.user_id = 18 AND checkup_header.is_complete = 0
    """
    return db.query(checkup_headers.CheckupHeadersDB.id).\
        filter(checkup_headers.CheckupHeadersDB.user_id == user_id,
               checkup_headers.CheckupHeadersDB.is_complete == is_complete).count()


"""
{
  "user_id": 18,
  "user_name": "Иванов И.И.",
  "facility_id": 1,
  "facility_name": "Пушкин",
  "route_id": 2,
  "route_name": "Маршрут 1",
  "time_start": "2023-02-02 15:08:18"
}
"""
def create_checkup_by_user_id(db: Session, header: CheckupHeaderCreate):
    db_checkup_header = checkup_headers.CheckupHeadersDB(user_id=header.user_id,
                                                         user_name=header.user_name,
                                                         facility_id=header.facility_id,
                                                         facility_name=header.facility_name,
                                                         route_id=header.route_id,
                                                         route_name=header.route_name,
                                                         time_start=header.time_start,
                                                         time_finish=None,
                                                         is_complete=header.is_complete)

    create_base(db, db_checkup_header)
    return db_checkup_header


def update_checkup_header_for_id(db: Session, checkup_headers_id: int,  value: CheckupHeaderUpdate):
    try:
        db.query(checkup_headers.CheckupHeadersDB).filter(checkup_headers.CheckupHeadersDB.id == checkup_headers_id).\
        update({"time_finish": value.time_finish, "is_complete": value.is_complete})
        db.commit()
        return {"detail": "success"}
    except:
        return {"detail": "fail"}
