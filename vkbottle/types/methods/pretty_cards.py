# Generated with love
import typing
import enum
from vkbottle.types import responses
from .access import APIAccessibility
from .method import BaseMethod


class PrettycardsCreate(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(
        self,
        owner_id: int,
        photo: str,
        title: str,
        link: str,
        price: str,
        price_old: str,
        button: str,
    ):
        """ prettyCards.create
        From Vk Docs: 
        Access from user token(s)
        :param owner_id: 
        :param photo: 
        :param title: 
        :param link: 
        :param price: 
        :param price_old: 
        :param button: 
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("prettyCards.create", params)


class PrettycardsDelete(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, owner_id: int, card_id: int):
        """ prettyCards.delete
        From Vk Docs: 
        Access from user token(s)
        :param owner_id: 
        :param card_id: 
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("prettyCards.delete", params)


class PrettycardsEdit(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(
        self,
        owner_id: int,
        card_id: int,
        photo: str,
        title: str,
        link: str,
        price: str,
        price_old: str,
        button: str,
    ):
        """ prettyCards.edit
        From Vk Docs: 
        Access from user token(s)
        :param owner_id: 
        :param card_id: 
        :param photo: 
        :param title: 
        :param link: 
        :param price: 
        :param price_old: 
        :param button: 
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("prettyCards.edit", params)


class PrettycardsGet(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, owner_id: int, offset: int, count: int):
        """ prettyCards.get
        From Vk Docs: 
        Access from user token(s)
        :param owner_id: 
        :param offset: 
        :param count: 
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("prettyCards.get", params)


class PrettycardsGetById(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, owner_id: int, card_ids: typing.List):
        """ prettyCards.getById
        From Vk Docs: 
        Access from user token(s)
        :param owner_id: 
        :param card_ids: 
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("prettyCards.getById", params)


class PrettycardsGetUploadURL(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self,):
        """ prettyCards.getUploadURL
        From Vk Docs: 
        Access from user token(s)
        
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("prettyCards.getUploadURL", params)


class Prettycards:
    def __init__(self, request):
        self.create = PrettycardsCreate(request)
        self.delete = PrettycardsDelete(request)
        self.edit = PrettycardsEdit(request)
        self.get = PrettycardsGet(request)
        self.get_by_id = PrettycardsGetById(request)
        self.get_upload_u_r_l = PrettycardsGetUploadURL(request)
