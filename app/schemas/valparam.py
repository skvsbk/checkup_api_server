from pydantic import BaseModel


class ValParamBase(BaseModel):
    name: str
    unit_id: int
    nfc_id: int
    min_value: float
    max_value: float


class ValParamOut(ValParamBase):
    id: int

    class Config:
        orm_mode = True


class ValParamCreate(ValParamBase):
    pass
