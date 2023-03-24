from pydantic import BaseModel


class PlantBase(BaseModel):
    name: str
    facility_id: int


class PlantOut(PlantBase):
    id: int

    class Config:
        orm_mode = True


class PlantByNFCSerialOut(BaseModel):
    plant_name: str
    facility_name: str

    class Config:
        orm_mode = True


class PlantByFacilityIdOut(BaseModel):
    plant_name: str
    nfc_serial: str | None
    active: bool | None

    class Config:
        orm_mode = True


class PlantForFreeOut(BaseModel):
    id: int
    name: str
    nfc_serial: str | None

    class Config:
        orm_mode = True


class PlantCreate(PlantBase):
    pass
