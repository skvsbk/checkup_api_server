from datetime import datetime
from pydantic import BaseModel


class CheckupDetailBase(BaseModel):
    header_id: int
    nfc_serial: str
    plant_id: int
    plant_name: str
    plant_description: str
    plant_description_params: str
    time_check: datetime


class CheckupDetailOut(CheckupDetailBase):
    id: int
    val_name: str | None
    val_min: float | None
    val_max: float | None
    unit_name: str | None
    val_fact: float | None
    note: str | None

    class Config:
        orm_mode = True


class CheckupDetailCreate(CheckupDetailBase):
    val_name: str | None = None
    val_min: float | None = None
    val_max: float | None = None
    unit_name: str | None = None
    val_fact: float | None = None
    note: str | None = None
