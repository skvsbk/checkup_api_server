from sqlalchemy.orm import Session
from app.schemas.routelink import RouteLinkCreate
from app.models import routelinks
from .base import create_base


def get_by_route_id(db: Session,  route_id: int):
    return db.query(routelinks.RouteLinksDB).filter(routelinks.RouteLinksDB.route_id == route_id).all()


def create_link(db: Session, link: RouteLinkCreate):
    db_link = routelinks.RouteLinksDB(route_id=link.route_id, nfc_id=link.nfc_id, order=link.order, active=link.active)
    create_base(db, db_link)
    return db_link


# def add_link():
#     return
#
#
# def remove_link():
#     return
#
#
# def update_kink():
#     return
