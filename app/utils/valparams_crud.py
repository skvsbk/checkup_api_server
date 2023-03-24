from sqlalchemy.orm import Session
from app.models import valparams, valunits, nfc, plants


def get_by_unit_id(db: Session, unit_id: int):
    return db.query(valparams.ValParamsDB).filter(valparams.ValParamsDB.unit_id == unit_id).first()


def get_params_by_nfc_serial(db: Session, nfc_serial: str):
    """
     SELECT val_params.min_value, val_params.max_value, val_units.name FROM `val_params`
    JOIN plants ON plants.id = val_params.plant_id
    JOIN nfc_tag ON nfc_tag.plant_id = val_params.plant_id
    JOIN val_units ON val_units.id = val_params.unit_id
    WHERE nfc_tag.nfc_serial = "53E9DC63200001"
    """
    res = db.query(valparams.ValParamsDB.id, valparams.ValParamsDB.name.label("name"), valparams.ValParamsDB.min_value,
                   valparams.ValParamsDB.max_value, valunits.ValUnitsDB.name.label("unit_name")). \
        join(plants.PlantsDB, plants.PlantsDB.id == valparams.ValParamsDB.plant_id). \
        join(nfc.NfcTagDB, nfc.NfcTagDB.plant_id == valparams.ValParamsDB.plant_id).\
        join(valunits.ValUnitsDB, valunits.ValUnitsDB.id == valparams.ValParamsDB.unit_id).\
        filter(nfc.NfcTagDB.nfc_serial == nfc_serial).first()
    return res


def get_all_params(db: Session, facility_id: str):
    """ SELECT * FROM val_params """
    res = db.query(valparams.ValParamsDB.id, valparams.ValParamsDB.name.label("name"), valparams.ValParamsDB.min_value,
                   valparams.ValParamsDB.max_value, valunits.ValUnitsDB.name.label("unit_name")).\
        join(valunits.ValUnitsDB, valunits.ValUnitsDB.id == valparams.ValParamsDB.unit_id).\
        filter(valparams.ValParamsDB.facility_id == facility_id).all()
    return res
