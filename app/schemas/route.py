from pydantic import BaseModel


class RouteBase(BaseModel):
    name: str
    plant_id: int
    active: bool


class RouteOut(RouteBase):
    route_id: int

    class Config:
        orm_mode = True


class RouteCreate(RouteBase):
    pass
