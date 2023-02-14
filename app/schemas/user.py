from pydantic import BaseModel


class UserBase(BaseModel):
    login: str
    # role_id: int
    name: str


class UserCreate(UserBase):
    password: str
    active: bool = True


class UserOut(UserBase):
    password: str
    role_name: str

    class Config:
        orm_mode = True
