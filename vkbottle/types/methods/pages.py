# Generated with love
import typing
import enum
from vkbottle.types import responses
from .access import APIAccessibility
from .method import BaseMethod


class PagesClearCache(BaseMethod):
    access_token_type: APIAccessibility = [
        APIAccessibility.USER,
        APIAccessibility.SERVICE,
    ]

    async def __call__(self, url: str):
        """ pages.clearCache
        From Vk Docs: Allows to clear the cache of particular 'external' pages which may be attached to VK posts.
        Access from user, service token(s)
        :param url: Address of the page where you need to refesh the cached version
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("pages.clearCache", params)


class PagesGet(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(
        self,
        owner_id: int,
        page_id: int,
        site_preview: bool,
        title: str,
        need_source: bool,
        need_html: bool,
    ):
        """ pages.get
        From Vk Docs: Returns information about a wiki page.
        Access from user token(s)
        :param owner_id: Page owner ID.
        :param page_id: Wiki page ID.
        :param global: '1' — to return information about a global wiki page
        :param site_preview: '1' — resulting wiki page is a preview for the attached link
        :param title: Wiki page title.
        :param need_source: 
        :param need_html: '1' — to return the page as HTML,
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("pages.get", params)


class PagesGetHistory(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, page_id: int, group_id: int, user_id: int):
        """ pages.getHistory
        From Vk Docs: Returns a list of all previous versions of a wiki page.
        Access from user token(s)
        :param page_id: Wiki page ID.
        :param group_id: ID of the community that owns the wiki page.
        :param user_id: 
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("pages.getHistory", params)


class PagesGetTitles(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, group_id: int):
        """ pages.getTitles
        From Vk Docs: Returns a list of wiki pages in a group.
        Access from user token(s)
        :param group_id: ID of the community that owns the wiki page.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("pages.getTitles", params)


class PagesGetVersion(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(
        self, version_id: int, group_id: int, user_id: int, need_html: bool
    ):
        """ pages.getVersion
        From Vk Docs: Returns the text of one of the previous versions of a wiki page.
        Access from user token(s)
        :param version_id: 
        :param group_id: ID of the community that owns the wiki page.
        :param user_id: 
        :param need_html: '1' — to return the page as HTML
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("pages.getVersion", params)


class PagesParseWiki(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, text: str, group_id: int):
        """ pages.parseWiki
        From Vk Docs: Returns HTML representation of the wiki markup.
        Access from user token(s)
        :param text: Text of the wiki page.
        :param group_id: ID of the group in the context of which this markup is interpreted.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("pages.parseWiki", params)


class PagesSave(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(
        self, text: str, page_id: int, group_id: int, user_id: int, title: str
    ):
        """ pages.save
        From Vk Docs: Saves the text of a wiki page.
        Access from user token(s)
        :param text: Text of the wiki page in wiki-format.
        :param page_id: Wiki page ID. The 'title' parameter can be passed instead of 'pid'.
        :param group_id: ID of the community that owns the wiki page.
        :param user_id: User ID
        :param title: Wiki page title.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("pages.save", params)


class PagesSaveAccess(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(
        self, page_id: int, group_id: int, user_id: int, view: int, edit: int
    ):
        """ pages.saveAccess
        From Vk Docs: Saves modified read and edit access settings for a wiki page.
        Access from user token(s)
        :param page_id: Wiki page ID.
        :param group_id: ID of the community that owns the wiki page.
        :param user_id: 
        :param view: Who can view the wiki page: '1' — only community members, '2' — all users can view the page, '0' — only community managers
        :param edit: Who can edit the wiki page: '1' — only community members, '2' — all users can edit the page, '0' — only community managers
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("pages.saveAccess", params)


class Pages:
    def __init__(self, request):
        self.clear_cache = PagesClearCache(request)
        self.get = PagesGet(request)
        self.get_history = PagesGetHistory(request)
        self.get_titles = PagesGetTitles(request)
        self.get_version = PagesGetVersion(request)
        self.parse_wiki = PagesParseWiki(request)
        self.save = PagesSave(request)
        self.save_access = PagesSaveAccess(request)
