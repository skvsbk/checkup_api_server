from datetime import datetime

from pydantic import BaseModel
from pydantic.class_validators import Optional

class CheckupDetailBase(BaseModel):
    header_id: int
    nfc_serial: str
    plant_id: int
    plant_name: str
    time_check: datetime


class CheckupDetailOut(CheckupDetailBase):
    id: int
    val_name: str | None
    val_min: float | None
    val_max: float | None
    unit_name: str | None
    val_fact: float | None

    class Config:
        orm_mode = True


class CheckupDetailCreate(CheckupDetailBase):
    val_name: str = None
    val_min: float = None
    val_max: float = None
    unit_name: str = None
    val_fact: float = None
