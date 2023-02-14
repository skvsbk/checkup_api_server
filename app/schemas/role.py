from pydantic import BaseModel


class RoleBase(BaseModel):
    role_name: str


class RoleOut(RoleBase):
    id: int

    class Config:
        orm_mode = True


class RoleCreate(RoleBase):
    pass
