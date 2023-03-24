from sqlalchemy.orm import Session
from app.models import routes


def get_routes_by_facility_id(db: Session, facility_id: int):
    res = db.query(routes.RoutesDB).\
        filter(routes.RoutesDB.facility_id == facility_id, routes.RoutesDB.active == True).all()
    return res
