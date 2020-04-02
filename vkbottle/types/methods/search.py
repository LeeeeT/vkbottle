# Generated with love
import typing
import enum
from vkbottle.types import responses
from .access import APIAccessibility
from .method import BaseMethod


class SearchGetHints(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(
        self,
        q: str,
        offset: int,
        limit: int,
        filters: typing.List,
        fields: typing.List,
        search_global: bool,
    ):
        """ search.getHints
        From Vk Docs: Allows the programmer to do a quick search for any substring.
        Access from user token(s)
        :param q: Search query string.
        :param offset: Offset for querying specific result subset
        :param limit: Maximum number of results to return.
        :param filters: 
        :param fields: 
        :param search_global: 
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("search.getHints", params)


class Search:
    def __init__(self, request):
        self.get_hints = SearchGetHints(request)
