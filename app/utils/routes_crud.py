from sqlalchemy.orm import Session
from app.schemas.route import RouteCreate
from app.models import routes
from .base import create_base


def get_routes_by_facility_id(db: Session, facility_id: int):
    res = db.query(routes.RoutesDB).filter(routes.RoutesDB.facility_id == facility_id, routes.RoutesDB.active == True).all()
    return res


# def create_route(db: Session, route: RouteCreate):
#     db_route = routes.RoutesDB(name=route.name, facility_id=route.facility_id, active=route.active)
#     create_base(db, db_route)
#     return db_route


# def update():
#     return
#
#
# def delete():
#     return
