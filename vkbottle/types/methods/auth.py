# Generated with love
import typing
import enum
from vkbottle.types import responses
from .access import APIAccessibility
from .method import BaseMethod


class AuthCheckPhone(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER, APIAccessibility.OPEN]

    async def __call__(
        self, phone: str, client_id: int, client_secret: str, auth_by_phone: bool
    ) -> responses.auth.CheckPhone:
        """ auth.checkPhone
        From Vk Docs: Checks a user's phone number for correctness.
        Access from user, open token(s)
        :param phone: Phone number.
        :param client_id: User ID.
        :param client_secret: 
        :param auth_by_phone: 
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request(
            "auth.checkPhone", params, response_model=responses.auth.CheckPhone
        )


class AuthRestore(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER, APIAccessibility.OPEN]

    async def __call__(
        self, phone: str, last_name: str
    ) -> responses.auth.RestoreResponse:
        """ auth.restore
        From Vk Docs: Allows to restore account access using a code received via SMS. " This method is only available for apps with [vk.com/dev/auth_direct|Direct authorization] access. "
        Access from user, open token(s)
        :param phone: User phone number.
        :param last_name: User last name.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request(
            "auth.restore",
            params,
            response_model=responses.auth.RestoreResponse,
            raw_response=True,
        )


class Auth:
    def __init__(self, request):
        self.check_phone = AuthCheckPhone(request)
        self.restore = AuthRestore(request)
