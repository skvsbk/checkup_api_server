# from typing import Optional
from pydantic import BaseModel


class NFCTag(BaseModel):
    nfc_id: int = None
    nfc_serial: str
    plant_id: int
