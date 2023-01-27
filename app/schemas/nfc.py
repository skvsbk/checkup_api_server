
from pydantic import BaseModel


class NFCTagBase(BaseModel):
    nfc_serial: str
    plant_id: int


class NFCTagOut(NFCTagBase):
    id: int

    class Config:
        orm_mode = True


class NFCTagCreate(NFCTagBase):
    pass
