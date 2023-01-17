from fastapi import APIRouter, Depends
from app.utils.users import UserUtils, RoleUtils
from app.routers.depends import get_user_utils
from app.models.database import database
from typing import List
from app.schemas.user import User

router = APIRouter()

@router.get('/users', response_model=List[User])
async def get_users(
    users: UserUtils = Depends(get_user_utils),
    limit: int = 100,
    skip: int = 0):
    return await users.get_all(limit=limit, skip=skip)

@router.get('/users/{login}', response_model=User)
async def get_user_by_login(login: str, user: UserUtils = Depends(get_user_utils)) -> User:
    return await user.get_by_login(login)

#
# @router.get('/roles')
# async def get_roles(
#     roles: RoleUtils = Depends(get_user_utils),
#     limit: int = 100,
#     skip: int = 0):
#     return await roles.get_all(limit=limit, skip=skip)