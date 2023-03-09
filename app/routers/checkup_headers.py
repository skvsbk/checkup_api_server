from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..utils import checkup_headers_crud
from ..models.database import get_db
from ..schemas.checkup_header import CheckupHeaderCreate, CheckupHeaderOut


router = APIRouter()


# http://0.0.0.0:8000/checkup_headers/?user_id=18
# [
#   {
#     "user_id": 18,
#     "user_name": "Иванов И.И.",
#     "facility_name": "Пушкин",
#     "route_name": "Маршрут 1",
#     "time_start": "2023-02-02 15:08:18",
#     "id": 1,
#     "time_finish": null,
#     "is_complete": false
#   },...
# ]
@router.get('/', response_model=list[CheckupHeaderOut])
async def get_checkup_by_user_id(user_id: int, db: Session = Depends(get_db)):
    return checkup_headers_crud.get_checkup_by_user_id(db=db, user_id=user_id)


# http://0.0.0.0:8000/checkup_headers/last?user_id=18&limit=3
@router.get('/last', response_model=list[CheckupHeaderOut])
async def get_last_checkup_by_user_id(user_id: int, limit: int, db: Session = Depends(get_db)):
    return checkup_headers_crud.get_last_checkup_by_user_id(db=db, user_id=user_id, limit=limit)


# http://0.0.0.0:8000/checkup_headers/count/user_id/18
# {
#   "total": 5,
#   "finished": 1,
#   "not_finished": 4
# }
@router.get('/count/user_id/{user_id}')
async def get_count_checkup_by_user_id(user_id: int, db: Session = Depends(get_db)):
    total = checkup_headers_crud.get_total_checkup_by_user_id(db=db, user_id=user_id)
    finished = checkup_headers_crud.get_done_or_not_checkup_by_user_id(db=db, user_id=user_id, is_complete=True)
    not_finished = checkup_headers_crud.get_done_or_not_checkup_by_user_id(db=db, user_id=user_id, is_complete=False)
    return {"total": total, "finished": finished, "not_finished": not_finished}


# http://0.0.0.0:8000/checkup_headers/
#   -d '{
#   "user_id": 18,
#   "user_name": "Иванов И.И.",
#   "facility_name": "Пушкин",
#   "route_name": "Маршрут 1",
#   "time_start": "2023-02-02 19:08:18"
# }'
@router.post('/', response_model=CheckupHeaderOut)
def create_checkup_by_user_id(value: CheckupHeaderCreate, db: Session = Depends(get_db)):
    return checkup_headers_crud.create_checkup_by_user_id(db=db, header=value)
