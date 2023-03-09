from sqlalchemy.orm import Session
from .base import create_base
from ..schemas.checkup_detail import CheckupDetailCreate
from ..models import checkup_details



def get_checkup_details_by_header_id(db: Session,  header_id: int):
    return db.query(checkup_details.CheckupDetailsDB).filter(checkup_details.CheckupDetailsDB.header_id == header_id).all()



def create_checkup_details(db: Session, details: CheckupDetailCreate):
    db_checkup_details = checkup_details.CheckupDetailsDB(header_id=details.header_id,
                                                          nfc_serial=details.nfc_serial,
                                                          plant_id=details.plant_id,
                                                          plant_name=details.plant_name,
                                                          val_name=details.val_name,
                                                          time_check=details.time_check,
                                                          val_min=details.val_min,
                                                          val_max=details.val_max,
                                                          unit_name=details.unit_name,
                                                          val_fact=details.val_fact)

    create_base(db, db_checkup_details)
    return db_checkup_details


