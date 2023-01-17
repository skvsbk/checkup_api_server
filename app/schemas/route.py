# from typing import Optional
from pydantic import BaseModel


class Route(BaseModel):
    route_id: int = None
    name: str
    plant_id: int
    active: bool
