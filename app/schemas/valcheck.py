from pydantic import BaseModel


class ValCheckBase(BaseModel):
    value: float
    note: str
    param_id: int
    check_id: int


class ValCheckOut(ValCheckBase):
    valuecheck_id: int

    class Config:
        orm_mode = True


class ValCheckCreate(ValCheckBase):
    pass
