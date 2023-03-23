from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.utils import routelinks_crud
from app.models.database import get_db
from app.schemas.routelink import RouteLinkCreate, RouteLinkOut


router = APIRouter()

# http://0.0.0.0:8000/rolutelinks/2
# [
#   {
#     "id": 1,
#     "order": 10,
#     "nfc_serial": "53C5D463200001",
#     "val_name": "Объем чего-то",
#     "val_min": 1000,
#     "val_max": null,
#     "unit_name": "ml"
#   },...
# ]
@router.get('/{route_id}', response_model=list[RouteLinkOut])
def get_route_links_by_route_id(route_id: int, db: Session = Depends(get_db)):
    return routelinks_crud.get_route_links_by_route_id(db=db, route_id=route_id)

#
# @router.post('/', response_model=RouteLinkOut)
# def create_link(value: RouteLinkCreate, db: Session = Depends(get_db)):
#     return routelinks_crud.create_link(db=db, link=value)
