from datetime import datetime

from pydantic import BaseModel
from pydantic.class_validators import Optional


class CheckupHeaderBase(BaseModel):
    user_id: int
    user_name: str
    facility_name: str
    route_name: str
    time_start: datetime


class CheckupHeaderOut(CheckupHeaderBase):
    id: int
    time_finish: datetime | None
    is_complete: bool

    class Config:
        orm_mode = True


class CheckupHeaderCreate(CheckupHeaderBase):
    facility_id: int
    route_id: int
    time_finish: Optional[datetime] = None
    is_complete: bool = False


class CheckupHeaderUpdate(BaseModel):
    time_finish: datetime
    is_complete: bool
