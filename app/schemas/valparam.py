from pydantic import BaseModel


class ValParamBase(BaseModel):
    name: str
    unit_id: int
    nfc_id: int
    min_value: float
    max_value: float



class ValParamOut(BaseModel):
    id: int
    name: str
    min_value: float
    max_value: float
    unit_name: str

    class Config:
        orm_mode = True

class ValParamCreate(ValParamBase):
    pass
