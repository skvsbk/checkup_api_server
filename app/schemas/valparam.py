# from typing import Optional
from pydantic import BaseModel


class ValParam(BaseModel):
    param_id: int = None
    name: str
    unit_id: int
    nfc_id: int
    min_value: float
    max_value: float

