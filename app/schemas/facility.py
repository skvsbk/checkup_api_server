# from typing import Optional
from pydantic import BaseModel


class Facility(BaseModel):
    facility_id: int = None
    name: str