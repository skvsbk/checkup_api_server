from pydantic import BaseModel
# from app.models.roles import RoleDB


class UserBase(BaseModel):
    login: str
    # role_id: int
    name: str


class UserCreate(UserBase):
    password: str
    active: bool = True
    role_id: int


class UserOut(UserBase):
    id: int
    password: str
    name: str
    role_name: str

    class Config:
        orm_mode = True
