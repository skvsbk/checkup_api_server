# from typing import Optional
from pydantic import BaseModel


class ValCheck(BaseModel):
    valuecheck_id: int
    value: float
    note: str
    param_id: int
    check_id: int
