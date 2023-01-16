from fastapi import APIRouter

router = APIRouter()

@router.get('/')
async def get_facility():
    return {'facilitiy': 'facility'}