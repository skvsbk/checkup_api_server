# from typing import Optional
from pydantic import BaseModel


class ValUnit(BaseModel):
    unit_id: int = None
    name: str
