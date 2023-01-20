from pydantic import BaseModel


class RouteBase(BaseModel):
    name: str
    facility_id: int
    active: bool = True


class RouteOut(RouteBase):
    route_id: int

    class Config:
        orm_mode = True


class RouteCreate(RouteBase):
    pass
