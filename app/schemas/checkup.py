from pydantic import BaseModel


class CheckupBase(BaseModel):
    completed: bool = False
    route_id: int
    user_id: int
    t_start: int
    t_end: int


class CheckupOut(CheckupBase):
    checkup_id: int

    class Config:
        orm_mode = True


class CheckupCreate(CheckupBase):
    pass
