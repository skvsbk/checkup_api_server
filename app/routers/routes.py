from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.utils import routes_crud
from app.models.database import get_db
from app.schemas.route import RouteCreate, RouteOut

router = APIRouter()

# http://127.0.0.1:8000/routes/?facility_id=1
# [
#   {
#     "name": "Маршрут №1",
#     "facility_id": 1,
#     "active": true,
#     "id": 2
#   },
#   {
#     "name": "Маршрут №2",
#     "facility_id": 1,
#     "active": true,
#     "id": 3
#   }, .....
# ]

@router.get('/', response_model=list[RouteOut])
async def get_routes_by_facility_id(facility_id: int, db: Session = Depends(get_db)):
    return routes_crud.get_routes_by_facility_id(db=db, facility_id=facility_id)


# @router.post('/', response_model=RouteOut)
# def create_user(value: RouteCreate, db: Session = Depends(get_db)):
#     return routes_crud.create_route(db=db, route=value)
