from sqlalchemy.orm import Session
from app.models import routelinks, valunits, valparams, nfc, plants


def get_route_links_by_route_id(db: Session,  route_id: int):
    """
    SELECT route_links.id, route_links.order,
    plants.name AS plant_name, plants.description_plant AS plant_description,
    plants.description_params AS plant_description_params,
    route_links.plant_id AS plant_id,
    nfc_tag.nfc_serial AS nfc_serial,
    val_params.name AS val_name, val_params.min_value AS val_min,
    val_params.max_value AS val_max, val_units.name AS unit_name FROM route_links
    JOIN plants ON plants.id = route_links.plant_id
    LEFT JOIN nfc_tag ON nfc_tag.plant_id = route_links.plant_id
    LEFT JOIN val_params ON val_params.plant_id = plants.id
    LEFT JOIN val_units ON val_units.id = val_params.unit_id
    WHERE route_links.route_id = 6 AND route_links.active = 1  AND nfc_tag.nfc_serial
    ORDER BY route_links.order
    """
    res = db.query(routelinks.RouteLinksDB.id, routelinks.RouteLinksDB.order,
                   plants.PlantsDB.name.label("plant_name"),
                   plants.PlantsDB.description_plant.label("plant_description"),
                   plants.PlantsDB.description_params.label("plant_description_params"),
                   routelinks.RouteLinksDB.plant_id.label("plant_id"),
                   nfc.NfcTagDB.nfc_serial.label("nfc_serial"),
                   valparams.ValParamsDB.name.label("val_name"), valparams.ValParamsDB.min_value.label("val_min"),
                   valparams.ValParamsDB.max_value.label("val_max"), valunits.ValUnitsDB.name.label("unit_name")).\
        join(plants.PlantsDB, plants.PlantsDB.id == routelinks.RouteLinksDB.plant_id). \
        outerjoin(nfc.NfcTagDB, nfc.NfcTagDB.plant_id == routelinks.RouteLinksDB.plant_id). \
        outerjoin(valparams.ValParamsDB, valparams.ValParamsDB.plant_id == routelinks.RouteLinksDB.plant_id).\
        outerjoin(valunits.ValUnitsDB, valunits.ValUnitsDB.id == valparams.ValParamsDB.unit_id).\
        filter(routelinks.RouteLinksDB.route_id == route_id, routelinks.RouteLinksDB.active == True,
               nfc.NfcTagDB.nfc_serial != None).\
        order_by(routelinks.RouteLinksDB.order).all()
    return res
