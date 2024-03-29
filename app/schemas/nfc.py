from pydantic import BaseModel


class NFCTagBase(BaseModel):
    nfc_serial: str
    plant_id: int
    active: bool


class NFCTagOut(NFCTagBase):
    id: int

    class Config:
        orm_mode = True


class NFCTagForPlantOut(BaseModel):
    nfc_id: int
    nfc_active: bool
    plant_name: str

    class Config:
        orm_mode = True


class NFCTagCreate(NFCTagBase):
    pass
