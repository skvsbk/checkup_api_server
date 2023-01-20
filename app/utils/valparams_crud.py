from sqlalchemy.orm import Session
from .base import create_base
from ..schemas.valparam import ValParamCreate
from ..models import valparams



def get_by_unit_id(db: Session, unit_id: int):
    return db.query(valparams.ValParamsDB).filter(valparams.ValParamsDB.unit_id == unit_id).first()


def create_param(db: Session, param: ValParamCreate):
    db_param = valparams.ValParamsDB(name=param.name, unit_id=param.unit_id, nfc_id=param.nfc_id,
                                     min_value=param.min_value, max_value=param.max_value)
    try:
        create_base(db, db_param)
        return db_param
    except:
        return None


# def update():
#     return
#
#
# def delete():
#     return
