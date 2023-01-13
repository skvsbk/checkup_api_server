from fastapi import APIRouter

router = APIRouter()

@router.get('/')
async def get_nfc():
    return {'nfc': 'nfc'}