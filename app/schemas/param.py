from typing import Optional
from pydantic import BaseModel


class Param(BaseModel):
    param_id: int = None
    name: str
    unit_id: int
    nfc_id: int
    min_value: float
    max_value: float

class Unit(BaseModel):
    unit_id: int = None
    name: str

class CheckingValue(BaseModel):
    valuecheck_id: int
    value: float
    note: str
    param_id: int
    check_id: int
