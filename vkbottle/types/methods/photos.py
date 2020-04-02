# Generated with love
import typing
import enum
from vkbottle.types import responses
from .access import APIAccessibility
from .method import BaseMethod


class PhotosConfirmTag(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, owner_id: int, photo_id: str, tag_id: int):
        """ photos.confirmTag
        From Vk Docs: Confirms a tag on a photo.
        Access from user token(s)
        :param owner_id: ID of the user or community that owns the photo.
        :param photo_id: Photo ID.
        :param tag_id: Tag ID.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("photos.confirmTag", params)


class PhotosCopy(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, owner_id: int, photo_id: int, access_key: str):
        """ photos.copy
        From Vk Docs: Allows to copy a photo to the "Saved photos" album
        Access from user token(s)
        :param owner_id: photo's owner ID
        :param photo_id: photo ID
        :param access_key: for private photos
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("photos.copy", params)


class PhotosCreateAlbum(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(
        self,
        title: str,
        group_id: int,
        description: str,
        privacy_view: typing.List,
        privacy_comment: typing.List,
        upload_by_admins_only: bool,
        comments_disabled: bool,
    ):
        """ photos.createAlbum
        From Vk Docs: Creates an empty photo album.
        Access from user token(s)
        :param title: Album title.
        :param group_id: ID of the community in which the album will be created.
        :param description: Album description.
        :param privacy_view: 
        :param privacy_comment: 
        :param upload_by_admins_only: 
        :param comments_disabled: 
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("photos.createAlbum", params)


class PhotosCreateComment(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(
        self,
        owner_id: int,
        photo_id: int,
        message: str,
        attachments: typing.List,
        from_group: bool,
        reply_to_comment: int,
        sticker_id: int,
        access_key: str,
        guid: str,
    ):
        """ photos.createComment
        From Vk Docs: Adds a new comment on the photo.
        Access from user token(s)
        :param owner_id: ID of the user or community that owns the photo.
        :param photo_id: Photo ID.
        :param message: Comment text.
        :param attachments: (Required if 'message' is not set.) List of objects attached to the post, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — Media attachment owner ID. '<media_id>' — Media attachment ID. Example: "photo100172_166443618,photo66748_265827614"
        :param from_group: '1' — to post a comment from the community
        :param reply_to_comment: 
        :param sticker_id: 
        :param access_key: 
        :param guid: 
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("photos.createComment", params)


class PhotosDelete(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, owner_id: int, photo_id: int):
        """ photos.delete
        From Vk Docs: Deletes a photo.
        Access from user token(s)
        :param owner_id: ID of the user or community that owns the photo.
        :param photo_id: Photo ID.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("photos.delete", params)


class PhotosDeleteAlbum(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, album_id: int, group_id: int):
        """ photos.deleteAlbum
        From Vk Docs: Deletes a photo album belonging to the current user.
        Access from user token(s)
        :param album_id: Album ID.
        :param group_id: ID of the community that owns the album.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("photos.deleteAlbum", params)


class PhotosDeleteComment(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, owner_id: int, comment_id: int):
        """ photos.deleteComment
        From Vk Docs: Deletes a comment on the photo.
        Access from user token(s)
        :param owner_id: ID of the user or community that owns the photo.
        :param comment_id: Comment ID.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("photos.deleteComment", params)


class PhotosEdit(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(
        self,
        owner_id: int,
        photo_id: int,
        caption: str,
        latitude: typing.Any,
        longitude: typing.Any,
        place_str: str,
        foursquare_id: str,
        delete_place: bool,
    ):
        """ photos.edit
        From Vk Docs: Edits the caption of a photo.
        Access from user token(s)
        :param owner_id: ID of the user or community that owns the photo.
        :param photo_id: Photo ID.
        :param caption: New caption for the photo. If this parameter is not set, it is considered to be equal to an empty string.
        :param latitude: 
        :param longitude: 
        :param place_str: 
        :param foursquare_id: 
        :param delete_place: 
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("photos.edit", params)


class PhotosEditAlbum(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(
        self,
        album_id: int,
        title: str,
        description: str,
        owner_id: int,
        privacy_view: typing.List,
        privacy_comment: typing.List,
        upload_by_admins_only: bool,
        comments_disabled: bool,
    ):
        """ photos.editAlbum
        From Vk Docs: Edits information about a photo album.
        Access from user token(s)
        :param album_id: ID of the photo album to be edited.
        :param title: New album title.
        :param description: New album description.
        :param owner_id: ID of the user or community that owns the album.
        :param privacy_view: 
        :param privacy_comment: 
        :param upload_by_admins_only: 
        :param comments_disabled: 
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("photos.editAlbum", params)


class PhotosEditComment(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(
        self, owner_id: int, comment_id: int, message: str, attachments: typing.List
    ):
        """ photos.editComment
        From Vk Docs: Edits a comment on a photo.
        Access from user token(s)
        :param owner_id: ID of the user or community that owns the photo.
        :param comment_id: Comment ID.
        :param message: New text of the comment.
        :param attachments: (Required if 'message' is not set.) List of objects attached to the post, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — Media attachment owner ID. '<media_id>' — Media attachment ID. Example: "photo100172_166443618,photo66748_265827614"
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("photos.editComment", params)


class PhotosGet(BaseMethod):
    access_token_type: APIAccessibility = [
        APIAccessibility.USER,
        APIAccessibility.SERVICE,
    ]

    async def __call__(
        self,
        owner_id: int,
        album_id: str,
        photo_ids: typing.List,
        rev: bool,
        extended: bool,
        feed_type: str,
        feed: int,
        photo_sizes: bool,
        offset: int,
        count: int,
    ):
        """ photos.get
        From Vk Docs: Returns a list of a user's or community's photos.
        Access from user, service token(s)
        :param owner_id: ID of the user or community that owns the photos. Use a negative value to designate a community ID.
        :param album_id: Photo album ID. To return information about photos from service albums, use the following string values: 'profile, wall, saved'.
        :param photo_ids: Photo IDs.
        :param rev: Sort order: '1' — reverse chronological, '0' — chronological
        :param extended: '1' — to return additional 'likes', 'comments', and 'tags' fields, '0' — (default)
        :param feed_type: Type of feed obtained in 'feed' field of the method.
        :param feed: unixtime, that can be obtained with [vk.com/dev/newsfeed.get|newsfeed.get] method in date field to get all photos uploaded by the user on a specific day, or photos the user has been tagged on. Also, 'uid' parameter of the user the event happened with shall be specified.
        :param photo_sizes: '1' — to return photo sizes in a [vk.com/dev/photo_sizes|special format]
        :param offset: 
        :param count: 
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("photos.get", params)


class PhotosGetAlbums(BaseMethod):
    access_token_type: APIAccessibility = [
        APIAccessibility.USER,
        APIAccessibility.SERVICE,
    ]

    async def __call__(
        self,
        owner_id: int,
        album_ids: typing.List,
        offset: int,
        count: int,
        need_system: bool,
        need_covers: bool,
        photo_sizes: bool,
    ):
        """ photos.getAlbums
        From Vk Docs: Returns a list of a user's or community's photo albums.
        Access from user, service token(s)
        :param owner_id: ID of the user or community that owns the albums.
        :param album_ids: Album IDs.
        :param offset: Offset needed to return a specific subset of albums.
        :param count: Number of albums to return.
        :param need_system: '1' — to return system albums with negative IDs
        :param need_covers: '1' — to return an additional 'thumb_src' field, '0' — (default)
        :param photo_sizes: '1' — to return photo sizes in a
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("photos.getAlbums", params)


class PhotosGetAlbumsCount(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, user_id: int, group_id: int):
        """ photos.getAlbumsCount
        From Vk Docs: Returns the number of photo albums belonging to a user or community.
        Access from user token(s)
        :param user_id: User ID.
        :param group_id: Community ID.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("photos.getAlbumsCount", params)


class PhotosGetAll(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(
        self,
        owner_id: int,
        extended: bool,
        offset: int,
        count: int,
        photo_sizes: bool,
        no_service_albums: bool,
        need_hidden: bool,
        skip_hidden: bool,
    ):
        """ photos.getAll
        From Vk Docs: Returns a list of photos belonging to a user or community, in reverse chronological order.
        Access from user token(s)
        :param owner_id: ID of a user or community that owns the photos. Use a negative value to designate a community ID.
        :param extended: '1' — to return detailed information about photos
        :param offset: Offset needed to return a specific subset of photos. By default, '0'.
        :param count: Number of photos to return.
        :param photo_sizes: '1' – to return image sizes in [vk.com/dev/photo_sizes|special format].
        :param no_service_albums: '1' – to return photos only from standard albums, '0' – to return all photos including those in service albums, e.g., 'My wall photos' (default)
        :param need_hidden: '1' – to show information about photos being hidden from the block above the wall.
        :param skip_hidden: '1' – not to return photos being hidden from the block above the wall. Works only with owner_id>0, no_service_albums is ignored.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("photos.getAll", params)


class PhotosGetAllComments(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(
        self, owner_id: int, album_id: int, need_likes: bool, offset: int, count: int
    ):
        """ photos.getAllComments
        From Vk Docs: Returns a list of comments on a specific photo album or all albums of the user sorted in reverse chronological order.
        Access from user token(s)
        :param owner_id: ID of the user or community that owns the album(s).
        :param album_id: Album ID. If the parameter is not set, comments on all of the user's albums will be returned.
        :param need_likes: '1' — to return an additional 'likes' field, '0' — (default)
        :param offset: Offset needed to return a specific subset of comments. By default, '0'.
        :param count: Number of comments to return. By default, '20'. Maximum value, '100'.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("photos.getAllComments", params)


class PhotosGetById(BaseMethod):
    access_token_type: APIAccessibility = [
        APIAccessibility.USER,
        APIAccessibility.SERVICE,
    ]

    async def __call__(self, photos: typing.List, extended: bool, photo_sizes: bool):
        """ photos.getById
        From Vk Docs: Returns information about photos by their IDs.
        Access from user, service token(s)
        :param photos: IDs separated with a comma, that are IDs of users who posted photos and IDs of photos themselves with an underscore character between such IDs. To get information about a photo in the group album, you shall specify group ID instead of user ID. Example: "1_129207899,6492_135055734, , -20629724_271945303"
        :param extended: '1' — to return additional fields, '0' — (default)
        :param photo_sizes: '1' — to return photo sizes in a
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("photos.getById", params)


class PhotosGetChatUploadServer(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, chat_id: int, crop_x: int, crop_y: int, crop_width: int):
        """ photos.getChatUploadServer
        From Vk Docs: Returns an upload link for chat cover pictures.
        Access from user token(s)
        :param chat_id: ID of the chat for which you want to upload a cover photo.
        :param crop_x: 
        :param crop_y: 
        :param crop_width: Width (in pixels) of the photo after cropping.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("photos.getChatUploadServer", params)


class PhotosGetComments(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(
        self,
        owner_id: int,
        photo_id: int,
        need_likes: bool,
        start_comment_id: int,
        offset: int,
        count: int,
        sort: str,
        access_key: str,
        extended: bool,
        fields: typing.List,
    ):
        """ photos.getComments
        From Vk Docs: Returns a list of comments on a photo.
        Access from user token(s)
        :param owner_id: ID of the user or community that owns the photo.
        :param photo_id: Photo ID.
        :param need_likes: '1' — to return an additional 'likes' field, '0' — (default)
        :param start_comment_id: 
        :param offset: Offset needed to return a specific subset of comments. By default, '0'.
        :param count: Number of comments to return.
        :param sort: Sort order: 'asc' — old first, 'desc' — new first
        :param access_key: 
        :param extended: 
        :param fields: 
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("photos.getComments", params)


class PhotosGetMarketAlbumUploadServer(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, group_id: int):
        """ photos.getMarketAlbumUploadServer
        From Vk Docs: Returns the server address for market album photo upload.
        Access from user token(s)
        :param group_id: Community ID.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("photos.getMarketAlbumUploadServer", params)


class PhotosGetMarketUploadServer(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(
        self, group_id: int, main_photo: bool, crop_x: int, crop_y: int, crop_width: int
    ):
        """ photos.getMarketUploadServer
        From Vk Docs: Returns the server address for market photo upload.
        Access from user token(s)
        :param group_id: Community ID.
        :param main_photo: '1' if you want to upload the main item photo.
        :param crop_x: X coordinate of the crop left upper corner.
        :param crop_y: Y coordinate of the crop left upper corner.
        :param crop_width: Width of the cropped photo in px.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("photos.getMarketUploadServer", params)


class PhotosGetMessagesUploadServer(BaseMethod):
    access_token_type: APIAccessibility = [
        APIAccessibility.USER,
        APIAccessibility.GROUP,
    ]

    async def __call__(self, peer_id: int):
        """ photos.getMessagesUploadServer
        From Vk Docs: Returns the server address for photo upload in a private message for a user.
        Access from user, group token(s)
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'Chat ID', e.g. '2000000001'. For community: '- Community ID', e.g. '-12345'. "
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("photos.getMessagesUploadServer", params)


class PhotosGetNewTags(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, offset: int, count: int):
        """ photos.getNewTags
        From Vk Docs: Returns a list of photos with tags that have not been viewed.
        Access from user token(s)
        :param offset: Offset needed to return a specific subset of photos.
        :param count: Number of photos to return.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("photos.getNewTags", params)


class PhotosGetOwnerCoverPhotoUploadServer(BaseMethod):
    access_token_type: APIAccessibility = [
        APIAccessibility.USER,
        APIAccessibility.GROUP,
    ]

    async def __call__(
        self, group_id: int, crop_x: int, crop_y: int, crop_x2: int, crop_y2: int
    ):
        """ photos.getOwnerCoverPhotoUploadServer
        From Vk Docs: Returns the server address for owner cover upload.
        Access from user, group token(s)
        :param group_id: ID of community that owns the album (if the photo will be uploaded to a community album).
        :param crop_x: X coordinate of the left-upper corner
        :param crop_y: Y coordinate of the left-upper corner
        :param crop_x2: X coordinate of the right-bottom corner
        :param crop_y2: Y coordinate of the right-bottom corner
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("photos.getOwnerCoverPhotoUploadServer", params)


class PhotosGetOwnerPhotoUploadServer(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, owner_id: int):
        """ photos.getOwnerPhotoUploadServer
        From Vk Docs: Returns an upload server address for a profile or community photo.
        Access from user token(s)
        :param owner_id: identifier of a community or current user. "Note that community id must be negative. 'owner_id=1' – user, 'owner_id=-1' – community, "
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("photos.getOwnerPhotoUploadServer", params)


class PhotosGetTags(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, owner_id: int, photo_id: int, access_key: str):
        """ photos.getTags
        From Vk Docs: Returns a list of tags on a photo.
        Access from user token(s)
        :param owner_id: ID of the user or community that owns the photo.
        :param photo_id: Photo ID.
        :param access_key: 
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("photos.getTags", params)


class PhotosGetUploadServer(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, group_id: int, album_id: int):
        """ photos.getUploadServer
        From Vk Docs: Returns the server address for photo upload.
        Access from user token(s)
        :param group_id: ID of community that owns the album (if the photo will be uploaded to a community album).
        :param album_id: 
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("photos.getUploadServer", params)


class PhotosGetUserPhotos(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(
        self, user_id: int, offset: int, count: int, extended: bool, sort: str
    ):
        """ photos.getUserPhotos
        From Vk Docs: Returns a list of photos in which a user is tagged.
        Access from user token(s)
        :param user_id: User ID.
        :param offset: Offset needed to return a specific subset of photos. By default, '0'.
        :param count: Number of photos to return. Maximum value is 1000.
        :param extended: '1' — to return an additional 'likes' field, '0' — (default)
        :param sort: Sort order: '1' — by date the tag was added in ascending order, '0' — by date the tag was added in descending order
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("photos.getUserPhotos", params)


class PhotosGetWallUploadServer(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, group_id: int):
        """ photos.getWallUploadServer
        From Vk Docs: Returns the server address for photo upload onto a user's wall.
        Access from user token(s)
        :param group_id: ID of community to whose wall the photo will be uploaded.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("photos.getWallUploadServer", params)


class PhotosMakeCover(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, owner_id: int, photo_id: int, album_id: int):
        """ photos.makeCover
        From Vk Docs: Makes a photo into an album cover.
        Access from user token(s)
        :param owner_id: ID of the user or community that owns the photo.
        :param photo_id: Photo ID.
        :param album_id: Album ID.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("photos.makeCover", params)


class PhotosMove(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, owner_id: int, target_album_id: int, photo_id: int):
        """ photos.move
        From Vk Docs: Moves a photo from one album to another.
        Access from user token(s)
        :param owner_id: ID of the user or community that owns the photo.
        :param target_album_id: ID of the album to which the photo will be moved.
        :param photo_id: Photo ID.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("photos.move", params)


class PhotosPutTag(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(
        self,
        owner_id: int,
        photo_id: int,
        user_id: int,
        x: typing.Any,
        y: typing.Any,
        x2: typing.Any,
        y2: typing.Any,
    ):
        """ photos.putTag
        From Vk Docs: Adds a tag on the photo.
        Access from user token(s)
        :param owner_id: ID of the user or community that owns the photo.
        :param photo_id: Photo ID.
        :param user_id: ID of the user to be tagged.
        :param x: Upper left-corner coordinate of the tagged area (as a percentage of the photo's width).
        :param y: Upper left-corner coordinate of the tagged area (as a percentage of the photo's height).
        :param x2: Lower right-corner coordinate of the tagged area (as a percentage of the photo's width).
        :param y2: Lower right-corner coordinate of the tagged area (as a percentage of the photo's height).
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("photos.putTag", params)


class PhotosRemoveTag(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, owner_id: int, photo_id: int, tag_id: int):
        """ photos.removeTag
        From Vk Docs: Removes a tag from a photo.
        Access from user token(s)
        :param owner_id: ID of the user or community that owns the photo.
        :param photo_id: Photo ID.
        :param tag_id: Tag ID.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("photos.removeTag", params)


class PhotosReorderAlbums(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, owner_id: int, album_id: int, before: int, after: int):
        """ photos.reorderAlbums
        From Vk Docs: Reorders the album in the list of user albums.
        Access from user token(s)
        :param owner_id: ID of the user or community that owns the album.
        :param album_id: Album ID.
        :param before: ID of the album before which the album in question shall be placed.
        :param after: ID of the album after which the album in question shall be placed.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("photos.reorderAlbums", params)


class PhotosReorderPhotos(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, owner_id: int, photo_id: int, before: int, after: int):
        """ photos.reorderPhotos
        From Vk Docs: Reorders the photo in the list of photos of the user album.
        Access from user token(s)
        :param owner_id: ID of the user or community that owns the photo.
        :param photo_id: Photo ID.
        :param before: ID of the photo before which the photo in question shall be placed.
        :param after: ID of the photo after which the photo in question shall be placed.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("photos.reorderPhotos", params)


class PhotosReport(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, owner_id: int, photo_id: int, reason: int):
        """ photos.report
        From Vk Docs: Reports (submits a complaint about) a photo.
        Access from user token(s)
        :param owner_id: ID of the user or community that owns the photo.
        :param photo_id: Photo ID.
        :param reason: Reason for the complaint: '0' – spam, '1' – child pornography, '2' – extremism, '3' – violence, '4' – drug propaganda, '5' – adult material, '6' – insult, abuse
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("photos.report", params)


class PhotosReportComment(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, owner_id: int, comment_id: int, reason: int):
        """ photos.reportComment
        From Vk Docs: Reports (submits a complaint about) a comment on a photo.
        Access from user token(s)
        :param owner_id: ID of the user or community that owns the photo.
        :param comment_id: ID of the comment being reported.
        :param reason: Reason for the complaint: '0' – spam, '1' – child pornography, '2' – extremism, '3' – violence, '4' – drug propaganda, '5' – adult material, '6' – insult, abuse
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("photos.reportComment", params)


class PhotosRestore(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, owner_id: int, photo_id: int):
        """ photos.restore
        From Vk Docs: Restores a deleted photo.
        Access from user token(s)
        :param owner_id: ID of the user or community that owns the photo.
        :param photo_id: Photo ID.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("photos.restore", params)


class PhotosRestoreComment(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, owner_id: int, comment_id: int):
        """ photos.restoreComment
        From Vk Docs: Restores a deleted comment on a photo.
        Access from user token(s)
        :param owner_id: ID of the user or community that owns the photo.
        :param comment_id: ID of the deleted comment.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("photos.restoreComment", params)


class PhotosSave(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(
        self,
        album_id: int,
        group_id: int,
        server: int,
        photos_list: str,
        hash: str,
        latitude: typing.Any,
        longitude: typing.Any,
        caption: str,
    ):
        """ photos.save
        From Vk Docs: Saves photos after successful uploading.
        Access from user token(s)
        :param album_id: ID of the album to save photos to.
        :param group_id: ID of the community to save photos to.
        :param server: Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        :param photos_list: Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        :param hash: Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        :param latitude: Geographical latitude, in degrees (from '-90' to '90').
        :param longitude: Geographical longitude, in degrees (from '-180' to '180').
        :param caption: Text describing the photo. 2048 digits max.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("photos.save", params)


class PhotosSaveMarketAlbumPhoto(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, group_id: int, photo: str, server: int, hash: str):
        """ photos.saveMarketAlbumPhoto
        From Vk Docs: Saves market album photos after successful uploading.
        Access from user token(s)
        :param group_id: Community ID.
        :param photo: Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        :param server: Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        :param hash: Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("photos.saveMarketAlbumPhoto", params)


class PhotosSaveMarketPhoto(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(
        self,
        group_id: int,
        photo: str,
        server: int,
        hash: str,
        crop_data: str,
        crop_hash: str,
    ):
        """ photos.saveMarketPhoto
        From Vk Docs: Saves market photos after successful uploading.
        Access from user token(s)
        :param group_id: Community ID.
        :param photo: Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        :param server: Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        :param hash: Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        :param crop_data: Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        :param crop_hash: Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("photos.saveMarketPhoto", params)


class PhotosSaveMessagesPhoto(BaseMethod):
    access_token_type: APIAccessibility = [
        APIAccessibility.USER,
        APIAccessibility.GROUP,
    ]

    async def __call__(self, photo: str, server: int, hash: str):
        """ photos.saveMessagesPhoto
        From Vk Docs: Saves a photo after being successfully uploaded. URL obtained with [vk.com/dev/photos.getMessagesUploadServer|photos.getMessagesUploadServer] method.
        Access from user, group token(s)
        :param photo: Parameter returned when the photo is [vk.com/dev/upload_files|uploaded to the server].
        :param server: 
        :param hash: 
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("photos.saveMessagesPhoto", params)


class PhotosSaveOwnerCoverPhoto(BaseMethod):
    access_token_type: APIAccessibility = [
        APIAccessibility.USER,
        APIAccessibility.GROUP,
    ]

    async def __call__(self, hash: str, photo: str):
        """ photos.saveOwnerCoverPhoto
        From Vk Docs: Saves cover photo after successful uploading.
        Access from user, group token(s)
        :param hash: Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        :param photo: Parameter returned when photos are [vk.com/dev/upload_files|uploaded to server].
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("photos.saveOwnerCoverPhoto", params)


class PhotosSaveOwnerPhoto(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, server: str, hash: str, photo: str):
        """ photos.saveOwnerPhoto
        From Vk Docs: Saves a profile or community photo. Upload URL can be got with the [vk.com/dev/photos.getOwnerPhotoUploadServer|photos.getOwnerPhotoUploadServer] method.
        Access from user token(s)
        :param server: parameter returned after [vk.com/dev/upload_files|photo upload].
        :param hash: parameter returned after [vk.com/dev/upload_files|photo upload].
        :param photo: parameter returned after [vk.com/dev/upload_files|photo upload].
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("photos.saveOwnerPhoto", params)


class PhotosSaveWallPhoto(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(
        self,
        user_id: int,
        group_id: int,
        photo: str,
        server: int,
        hash: str,
        latitude: typing.Any,
        longitude: typing.Any,
        caption: str,
    ):
        """ photos.saveWallPhoto
        From Vk Docs: Saves a photo to a user's or community's wall after being uploaded.
        Access from user token(s)
        :param user_id: ID of the user on whose wall the photo will be saved.
        :param group_id: ID of community on whose wall the photo will be saved.
        :param photo: Parameter returned when the the photo is [vk.com/dev/upload_files|uploaded to the server].
        :param server: 
        :param hash: 
        :param latitude: Geographical latitude, in degrees (from '-90' to '90').
        :param longitude: Geographical longitude, in degrees (from '-180' to '180').
        :param caption: Text describing the photo. 2048 digits max.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("photos.saveWallPhoto", params)


class PhotosSearch(BaseMethod):
    access_token_type: APIAccessibility = [
        APIAccessibility.USER,
        APIAccessibility.SERVICE,
    ]

    async def __call__(
        self,
        q: str,
        lat: typing.Any,
        long: typing.Any,
        start_time: int,
        end_time: int,
        sort: int,
        offset: int,
        count: int,
        radius: int,
    ):
        """ photos.search
        From Vk Docs: Returns a list of photos.
        Access from user, service token(s)
        :param q: Search query string.
        :param lat: Geographical latitude, in degrees (from '-90' to '90').
        :param long: Geographical longitude, in degrees (from '-180' to '180').
        :param start_time: 
        :param end_time: 
        :param sort: Sort order:
        :param offset: Offset needed to return a specific subset of photos.
        :param count: Number of photos to return.
        :param radius: Radius of search in meters (works very approximately). Available values: '10', '100', '800', '6000', '50000'.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("photos.search", params)


class Photos:
    def __init__(self, request):
        self.confirm_tag = PhotosConfirmTag(request)
        self.copy = PhotosCopy(request)
        self.create_album = PhotosCreateAlbum(request)
        self.create_comment = PhotosCreateComment(request)
        self.delete = PhotosDelete(request)
        self.delete_album = PhotosDeleteAlbum(request)
        self.delete_comment = PhotosDeleteComment(request)
        self.edit = PhotosEdit(request)
        self.edit_album = PhotosEditAlbum(request)
        self.edit_comment = PhotosEditComment(request)
        self.get = PhotosGet(request)
        self.get_albums = PhotosGetAlbums(request)
        self.get_albums_count = PhotosGetAlbumsCount(request)
        self.get_all = PhotosGetAll(request)
        self.get_all_comments = PhotosGetAllComments(request)
        self.get_by_id = PhotosGetById(request)
        self.get_chat_upload_server = PhotosGetChatUploadServer(request)
        self.get_comments = PhotosGetComments(request)
        self.get_market_album_upload_server = PhotosGetMarketAlbumUploadServer(request)
        self.get_market_upload_server = PhotosGetMarketUploadServer(request)
        self.get_messages_upload_server = PhotosGetMessagesUploadServer(request)
        self.get_new_tags = PhotosGetNewTags(request)
        self.get_owner_cover_photo_upload_server = PhotosGetOwnerCoverPhotoUploadServer(
            request
        )
        self.get_owner_photo_upload_server = PhotosGetOwnerPhotoUploadServer(request)
        self.get_tags = PhotosGetTags(request)
        self.get_upload_server = PhotosGetUploadServer(request)
        self.get_user_photos = PhotosGetUserPhotos(request)
        self.get_wall_upload_server = PhotosGetWallUploadServer(request)
        self.make_cover = PhotosMakeCover(request)
        self.move = PhotosMove(request)
        self.put_tag = PhotosPutTag(request)
        self.remove_tag = PhotosRemoveTag(request)
        self.reorder_albums = PhotosReorderAlbums(request)
        self.reorder_photos = PhotosReorderPhotos(request)
        self.report = PhotosReport(request)
        self.report_comment = PhotosReportComment(request)
        self.restore = PhotosRestore(request)
        self.restore_comment = PhotosRestoreComment(request)
        self.save = PhotosSave(request)
        self.save_market_album_photo = PhotosSaveMarketAlbumPhoto(request)
        self.save_market_photo = PhotosSaveMarketPhoto(request)
        self.save_messages_photo = PhotosSaveMessagesPhoto(request)
        self.save_owner_cover_photo = PhotosSaveOwnerCoverPhoto(request)
        self.save_owner_photo = PhotosSaveOwnerPhoto(request)
        self.save_wall_photo = PhotosSaveWallPhoto(request)
        self.search = PhotosSearch(request)
