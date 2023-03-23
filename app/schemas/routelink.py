from pydantic import BaseModel


class RouteLinkBase(BaseModel):
    nfc_id: int
    route_id: int
    order: int
    active: bool = True


class RouteLinkOut(BaseModel):
    id: int
    order: int
    nfc_serial: str
    plant_name: str | None
    plant_id: int | None
    val_name: str | None
    val_min: float | None
    val_max: float | None
    unit_name: str | None


    class Config:
        orm_mode = True


class RouteLinkCreate(RouteLinkBase):
    pass
