from fastapi import APIRouter

router = APIRouter()

@router.get('/')
async def get_param():
    return {'param': 'param_1'}