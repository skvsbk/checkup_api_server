from typing import Optional
from pydantic import BaseModel, validator

# to get user
class User(BaseModel):
    user_id: Optional[int] = None
    login: str
    password: str
    role_id: int
    name: str
    active: bool

# to add new user
class UserIn(BaseModel):
    login: str
    password: str
    password2: str
    role_id: int
    name: str
    active: bool = True

    @validator("password2")
    def password_match(cls, v, values, **kwargs):
        if 'password' in values and v != values['password']:
            raise ValueError("Passwords does not match")
        return v

class Role(BaseModel):
    role_id: int
    name: str
