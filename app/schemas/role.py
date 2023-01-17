from pydantic import BaseModel


class Role(BaseModel):
    role_id: int
    name: str
