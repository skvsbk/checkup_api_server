from .base import BaseUtil
from app.schemas.route import Route, RouteLink


class RouteUtils(BaseUtil):
    async def get_all(self):
        return

    async def create(self):
        return

    async def update(self):
        return

    async def delete(self):
        return


class RouteLinkUtils(BaseUtil):
    async def get_by_route_id(self):
        return

    async def add_link(self):
        return

    async def remove_link(self):
        return

    async def update_kink(self):
        return
