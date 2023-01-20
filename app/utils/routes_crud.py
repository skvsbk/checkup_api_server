from sqlalchemy.orm import Session
from .base import create_base
from ..schemas.route import RouteCreate
from ..models import routes


def get_by_facility_id(db: Session, facility_id: int):
    return db.query(routes.RoutesDB).filter(routes.RoutesDB.facility_id == facility_id).all()


def create_route(db: Session, route: RouteCreate):
    db_route = routes.RoutesDB(name=route.name, facility_id=route.facility_id, active=route.active)
    create_base(db, db_route)
    return db_route


# def update():
#     return
#
#
# def delete():
#     return
