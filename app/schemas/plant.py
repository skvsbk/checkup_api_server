from pydantic import BaseModel


class Plant(BaseModel):
    plant_id: int = None
    name: str
