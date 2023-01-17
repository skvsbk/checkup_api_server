from typing import List
from app.models.users import users, user_roles
from app.schemas.user import User, UserIn, Role
from .base import BaseUtil


class UserUtils(BaseUtil):
    async def get_all(self, limit: int, skip: int = 0) -> List[User]:
        return

    async def get_by_login(self, login: str) -> User:
        return

    async def create(self, u: UserIn) -> User:
        return

    async def update(self, u: UserIn) -> User:
        return


class RoleUtils(BaseUtil):
    async def get_all(self) -> Role:
        return

    async def create(self) -> Role:
        return

    async def update(self) -> Role:
        return
