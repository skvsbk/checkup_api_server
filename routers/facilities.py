from fastapi import APIRouter

router = APIRouter()

@router.get('/')
async def get_facilities():
    return {'facilities': 'facilities'}