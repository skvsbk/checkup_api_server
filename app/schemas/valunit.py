from pydantic import BaseModel


class ValUnitBase(BaseModel):
    name: str


class ValUnitOut(ValUnitBase):
    unit_id: int

    class Config:
        orm_mode = True


class ValUnitCreate(ValUnitBase):
    pass
