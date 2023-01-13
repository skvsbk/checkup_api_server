from typing import Optional
from pydantic import BaseModel


class Route(BaseModel):
    route_id: int = None
    name: str
    plant_id: int
    active: bool

class RouteLink(BaseModel):
    route_id: int
    nfc_id: int
    order_id: int
    active: bool