from pydantic import BaseModel


class Check(BaseModel):
    check_id: int = None
    note: str
    checkup_id: int
    nfc_id: int
