from pydantic import BaseModel


class RouteLinkBase(BaseModel):
    nfc_id: int
    order_id: int
    active: bool


class RouteLinkOut(RouteLinkBase):
    route_id: int

    class Config:
        orm_mode = True


class RouteLinkCreate(RouteLinkBase):
    pass
