from pydantic import BaseModel


class RouteLink(BaseModel):
    route_id: int
    nfc_id: int
    order_id: int
    active: bool
