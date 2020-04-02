# Generated with love
import typing
import enum
from vkbottle.types import responses
from .access import APIAccessibility
from .method import BaseMethod


class NotificationsGet(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(
        self,
        count: int,
        start_from: str,
        filters: typing.List,
        start_time: int,
        end_time: int,
    ):
        """ notifications.get
        From Vk Docs: Returns a list of notifications about other users' feedback to the current user's wall posts.
        Access from user token(s)
        :param count: Number of notifications to return.
        :param start_from: 
        :param filters: Type of notifications to return: 'wall' — wall posts, 'mentions' — mentions in wall posts, comments, or topics, 'comments' — comments to wall posts, photos, and videos, 'likes' — likes, 'reposted' — wall posts that are copied from the current user's wall, 'followers' — new followers, 'friends' — accepted friend requests
        :param start_time: Earliest timestamp (in Unix time) of a notification to return. By default, 24 hours ago.
        :param end_time: Latest timestamp (in Unix time) of a notification to return. By default, the current time.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("notifications.get", params)


class NotificationsMarkAsViewed(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self,):
        """ notifications.markAsViewed
        From Vk Docs: Resets the counter of new notifications about other users' feedback to the current user's wall posts.
        Access from user token(s)
        
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("notifications.markAsViewed", params)


class NotificationsSendMessage(BaseMethod):
    access_token_type: APIAccessibility = [
        APIAccessibility.USER,
        APIAccessibility.SERVICE,
    ]

    async def __call__(
        self, user_ids: typing.List, message: str, fragment: str, group_id: int
    ):
        """ notifications.sendMessage
        From Vk Docs: 
        Access from user, service token(s)
        :param user_ids: 
        :param message: 
        :param fragment: 
        :param group_id: 
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("notifications.sendMessage", params)


class Notifications:
    def __init__(self, request):
        self.get = NotificationsGet(request)
        self.mark_as_viewed = NotificationsMarkAsViewed(request)
        self.send_message = NotificationsSendMessage(request)
