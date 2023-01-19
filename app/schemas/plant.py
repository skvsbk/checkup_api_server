from pydantic import BaseModel


class PlantBase(BaseModel):
    name: str
    facility_id: int

class PlantOut(PlantBase):
    plant_id: int
    class Config:
        orm_mode = True

class PlantCreate(PlantBase):
    pass

