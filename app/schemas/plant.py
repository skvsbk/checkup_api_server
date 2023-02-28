from pydantic import BaseModel


class PlantBase(BaseModel):
    name: str
    facility_id: int


class PlantOut(PlantBase):
    id: int

    class Config:
        orm_mode = True

class PlantByNFCSerialOut(BaseModel):
    name: str

    class Config:
        orm_mode = True


class PlantCreate(PlantBase):
    pass
