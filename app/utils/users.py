from typing import List

from databases.interfaces import Record

from app.models.users import users, user_roles
from app.schemas.user import User, UserIn, Role
from .base import BaseUtil


class UserUtils(BaseUtil):
    async def get_all(self, limit: int, skip: int = 0):
        query = users.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query=query)

    async def get_by_login(self, login: str) -> User | None:
        query = users.select().where(users.c.login == login)
        return await self.database.fetch_one(query=query)

    async def create(self, u: UserIn) -> User:
        return

    async def update(self, u: UserIn) -> User:
        return


class RoleUtils(BaseUtil):
    async def get_all(self, limit: int, skip: int = 0) -> list[Record]:
        query = user_roles.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query=query)

    async def create(self) -> Role:
        return

    async def update(self) -> Role:
        return
