from fastapi import APIRouter
from ..schemas.valparam import ValParamOut

router = APIRouter()

@router.get('/params', response_model=ValParamOut)
async def get_param():
    return {'param': 'param_1'}