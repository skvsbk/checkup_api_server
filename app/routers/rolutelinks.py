from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.utils import routelinks_crud
from app.models.database import get_db
from app.schemas.routelink import RouteLinkOut


router = APIRouter()


# http://0.0.0.0:8000/rolutelinks/2
# [
#   {
#     "id": 14,
#     "order": 10,
#     "nfc_serial": "123",
#     "plant_name": "ЛОС",
#     "plant_description": "Локальные очистные сооружения",
#     "plant_description_params": "Общее состояние помещения и систем",
#     "plant_id": 50,
#     "val_name": "состояние помещения и систем",
#     "val_min": 14,
#     "val_max": 20,
#     "unit_name": "°C"
#   }, ...
# ]
@router.get('/{route_id}', response_model=list[RouteLinkOut])
def get_route_links_by_route_id(route_id: int, db: Session = Depends(get_db)):
    return routelinks_crud.get_route_links_by_route_id(db=db, route_id=route_id)
