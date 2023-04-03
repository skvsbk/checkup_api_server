from pydantic import BaseModel


class PlantBase(BaseModel):
    name: str
    description_plant: str
    description_params: str
    facility_id: int


class PlantOut(PlantBase):
    id: int

    class Config:
        orm_mode = True


class PlantByNFCSerialOut(BaseModel):
    plant_name: str
    facility_name: str
    description_plant: str | None
    description_params: str | None

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
