# from typing import Optional
from pydantic import BaseModel


class FacilityBase(BaseModel):
    name: str

class FacilityOut(FacilityBase):
    facility_id: int
    class Config:
        orm_mode = True

class FacilityCreate(FacilityBase):
    pass