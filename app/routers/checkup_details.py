from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..utils import checkup_details_crud
from ..models.database import get_db
from ..schemas.checkup_detail import CheckupDetailCreate, CheckupDetailOut


router = APIRouter()

# http://0.0.0.0:8000/checkup_details/?header_id=1
# [
#   {
#     "header_id": 1,
#     "nfc_serial": "000111222333",
#     "plant_id": 7,
#     "plant_name": "Водоподготовка",
#     "time_check": "2023-03-09T09:28:21",
#     "id": 1,
#     "val_name": "Давление",
#     "val_min": 1,
#     "val_max": 6,
#     "unit_name": "bar",
#     "val_fact": 3
#   },...
# ]

@router.get('/', response_model=list[CheckupDetailOut])
async def get_checkup_details_by_header_id(header_id: int, db: Session = Depends(get_db)):
    return checkup_details_crud.get_checkup_details_by_header_id(db=db, header_id=header_id)

# http://0.0.0.0:8000/checkup_details/
# {
#   "header_id": 1,
#   "nfc_serial": "45454545",
#   "plant_id": 4,
#   "plant_name": "1.006",
#   "time_check": "2023-03-09 09:36:22",
# Options:
#   "val_name": "Какой-то параметр",
#   "val_min": 2.5,
#   "val_max": 3.8,
#   "unit_name": "кг",
#   "val_fact": 4.2
# }
@router.post('/', response_model=CheckupDetailOut)
def create_checkup_details(value: CheckupDetailCreate, db: Session = Depends(get_db)):
    return checkup_details_crud.create_checkup_details(db=db, details=value)
