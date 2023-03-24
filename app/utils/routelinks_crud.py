from sqlalchemy.orm import Session
from app.models import routelinks, valunits, valparams, nfc, plants


def get_route_links_by_route_id(db: Session,  route_id: int):
    """
    SELECT plants.name AS plant_name, plants.id AS plant_id, route_links.id, route_links.order,
    nfc_tag.nfc_serial AS nfc_serial, val_params.name AS val_name,
    val_params.min_value AS val_min, val_params.max_value AS val_max, val_units.name AS unit_name FROM route_links
    JOIN nfc_tag ON nfc_tag.id = route_links.nfc_id
    JOIN plants ON plants.id = nfc_tag.plant_id
    LEFT JOIN val_params ON val_params.plant_id = plants.id
    LEFT JOIN val_units ON val_units.id = val_params.unit_id
    WHERE route_links.route_id = 2 AND route_links.active = 1
    ORDER BY route_links.order
    """
    res = db.query(routelinks.RouteLinksDB.id, routelinks.RouteLinksDB.order,
                   plants.PlantsDB.name.label("plant_name"), plants.PlantsDB.id.label("plant_id"),
                   nfc.NfcTagDB.nfc_serial.label("nfc_serial"),
                   valparams.ValParamsDB.name.label("val_name"), valparams.ValParamsDB.min_value.label("val_min"),
                   valparams.ValParamsDB.max_value.label("val_max"), valunits.ValUnitsDB.name.label("unit_name")).\
        join(nfc.NfcTagDB, nfc.NfcTagDB.id == routelinks.RouteLinksDB.nfc_id).\
        join(plants.PlantsDB, plants.PlantsDB.id == nfc.NfcTagDB.plant_id).\
        outerjoin(valparams.ValParamsDB, valparams.ValParamsDB.plant_id == plants.PlantsDB.id).\
        outerjoin(valunits.ValUnitsDB, valunits.ValUnitsDB.id == valparams.ValParamsDB.unit_id).\
        filter(routelinks.RouteLinksDB.route_id == route_id, routelinks.RouteLinksDB.active == True).\
        order_by(routelinks.RouteLinksDB.order).all()
    return res
