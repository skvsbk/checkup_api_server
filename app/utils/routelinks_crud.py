from sqlalchemy.orm import Session
from app.schemas.routelink import RouteLinkCreate
from app.models import routelinks, valunits, valparams, nfc
from .base import create_base


def get_route_links_by_route_id(db: Session,  route_id: int):
    """
    SELECT * FROM route_links
    JOIN nfc_tag ON nfc_tag.id = route_links.nfc_id
    LEFT JOIN val_params ON val_params.nfc_id = nfc_tag.id
    LEFT JOIN val_units ON val_units.id = val_params.unit_id
    WHERE route_links.route_id = 2 AND route_links.active = 1
    ORDER BY route_links.order
    """
    res = db.query(routelinks.RouteLinksDB.id, routelinks.RouteLinksDB.order, nfc.NfcTagDB.nfc_serial,
                   valparams.ValParamsDB.name.label("val_name"), valparams.ValParamsDB.min_value.label("val_min"),
                   valparams.ValParamsDB.max_value.label("val_ma["), valunits.ValUnitsDB.name.label("unit_name")).\
        join(nfc.NfcTagDB, nfc.NfcTagDB.id == routelinks.RouteLinksDB.nfc_id).\
        outerjoin(valparams.ValParamsDB, valparams.ValParamsDB.nfc_id == nfc.NfcTagDB.id).\
        outerjoin(valunits.ValUnitsDB, valunits.ValUnitsDB.id == valparams.ValParamsDB.unit_id).\
        filter(routelinks.RouteLinksDB.route_id == route_id, routelinks.RouteLinksDB.active == True).\
        order_by(routelinks.RouteLinksDB.order).all()
    return res


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
