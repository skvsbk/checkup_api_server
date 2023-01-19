from fastapi import APIRouter
from app.schemas.valparam import ValParam

router = APIRouter()

@router.get('/params', response_model=ValParam)
async def get_param():
    return {'param': 'param_1'}