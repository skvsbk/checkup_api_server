from pydantic import BaseModel


class RoleBase(BaseModel):
    name: str


class RoleOut(RoleBase):
    role_id: int

    class Config:
        orm_mode = True


class RoleCreate(RoleBase):
    pass
