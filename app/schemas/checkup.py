# from typing import Optional
from pydantic import BaseModel


class Checkup(BaseModel):
    checkup_id: int
    completed: bool
    route_id: int
    t_start: int
    t_end: int
