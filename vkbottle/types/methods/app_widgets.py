# Generated with love
import typing
import enum
from vkbottle.types import responses
from .access import APIAccessibility
from .method import BaseMethod


class AppwidgetsUpdate(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.GROUP]

    async def __call__(self, code: str, type: str):
        """ appWidgets.update
        From Vk Docs: Allows to update community app widget
        Access from group token(s)
        :param code: 
        :param type: 
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("appWidgets.update", params)


class Appwidgets:
    def __init__(self, request):
        self.update = AppwidgetsUpdate(request)
