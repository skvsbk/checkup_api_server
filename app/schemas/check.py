from datetime import datetime

from pydantic import BaseModel, validator


class CheckBase(BaseModel):
    note: str
    checkup_id: int
    nfc_id: int
    t_check: datetime


class CheckOut(CheckBase):
    id: int

    class Config:
        orm_mode = True


class CheckCreate(CheckBase):
    pass
