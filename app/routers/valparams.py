from fastapi import APIRouter
from app.schemas.valparam import Param

router = APIRouter()

@router.get('/params', response_model=Param)
async def get_param():
    return {'param': 'param_1'}