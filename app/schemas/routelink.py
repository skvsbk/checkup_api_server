from pydantic import BaseModel


class RouteLinkBase(BaseModel):
    nfc_id: int
    route_id: int
    order: int
    active: bool = True


class RouteLinkOut(RouteLinkBase):
    id: int

    class Config:
        orm_mode = True


class RouteLinkCreate(RouteLinkBase):
    pass
