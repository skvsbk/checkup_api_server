from typing import Optional
from pydantic import BaseModel


class Checkup(BaseModel):
    checkup_id: int
    completed: bool
    roite_id: int
    t_start: int
    t_end: int

class Check(BaseModel):
    check_id: int = None
    note: str
    checkup_id: int
    nfc_id: int
