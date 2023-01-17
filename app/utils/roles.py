# from typing import List
from databases.interfaces import Record
from app.models.roles import user_roles
from app.schemas.role import Role
from .base import BaseUtil


class RoleUtils(BaseUtil):
    async def get_all(self, limit: int, skip: int = 0) -> list[Record]:
        query = user_roles.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query=query)

    async def create(self) -> Role:
        return

    async def update(self) -> Role:
        return
