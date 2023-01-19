from pydantic import BaseModel


class CheckBase(BaseModel):
    note: str
    checkup_id: int
    nfc_id: int


class CheckOut(CheckBase):
    check_id: int

    class Config:
        orm_mode = True


class CheckCreate(CheckBase):
    pass
