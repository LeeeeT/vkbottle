# Generated with love
import typing
import enum
from vkbottle.types import responses
from .access import APIAccessibility
from .method import BaseMethod


class AccountBan(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, owner_id: int) -> responses.account.Ban:
        """ account.ban
        From Vk Docs: 
        Access from user token(s)
        :param owner_id: 
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request(
            "account.ban", params, response_model=responses.account.Ban
        )


class AccountChangePassword(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(
        self,
        restore_sid: str,
        change_password_hash: str,
        old_password: str,
        new_password: str,
    ) -> responses.account.ChangePassword:
        """ account.changePassword
        From Vk Docs: Changes a user password after access is successfully restored with the [vk.com/dev/auth.restore|auth.restore] method.
        Access from user token(s)
        :param restore_sid: Session id received after the [vk.com/dev/auth.restore|auth.restore] method is executed. (If the password is changed right after the access was restored)
        :param change_password_hash: Hash received after a successful OAuth authorization with a code got by SMS. (If the password is changed right after the access was restored)
        :param old_password: Current user password.
        :param new_password: New password that will be set as a current
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request(
            "account.changePassword",
            params,
            response_model=responses.account.ChangePassword,
        )


class AccountGetActiveOffers(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(
        self, offset: int, count: int
    ) -> responses.account.GetActiveOffers:
        """ account.getActiveOffers
        From Vk Docs: Returns a list of active ads (offers) which executed by the user will bring him/her respective number of votes to his balance in the application.
        Access from user token(s)
        :param offset: 
        :param count: Number of results to return.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request(
            "account.getActiveOffers",
            params,
            response_model=responses.account.GetActiveOffers,
        )


class AccountGetAppPermissions(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, user_id: int) -> responses.account.GetAppPermissions:
        """ account.getAppPermissions
        From Vk Docs: Gets settings of the user in this application.
        Access from user token(s)
        :param user_id: User ID whose settings information shall be got. By default: current user.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request(
            "account.getAppPermissions",
            params,
            response_model=responses.account.GetAppPermissions,
        )


class AccountGetBanned(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, offset: int, count: int) -> responses.account.GetBanned:
        """ account.getBanned
        From Vk Docs: Returns a user's blacklist.
        Access from user token(s)
        :param offset: Offset needed to return a specific subset of results.
        :param count: Number of results to return.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request(
            "account.getBanned", params, response_model=responses.account.GetBanned
        )


class AccountGetCounters(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, filter: typing.List) -> responses.account.GetCounters:
        """ account.getCounters
        From Vk Docs: Returns non-null values of user counters.
        Access from user token(s)
        :param filter: Counters to be returned.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request(
            "account.getCounters", params, response_model=responses.account.GetCounters
        )


class AccountGetInfo(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, fields: typing.List) -> responses.account.GetInfo:
        """ account.getInfo
        From Vk Docs: Returns current account info.
        Access from user token(s)
        :param fields: Fields to return. Possible values: *'country' — user country,, *'https_required' — is "HTTPS only" option enabled,, *'own_posts_default' — is "Show my posts only" option is enabled,, *'no_wall_replies' — are wall replies disabled or not,, *'intro' — is intro passed by user or not,, *'lang' — user language. By default: all.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request(
            "account.getInfo", params, response_model=responses.account.GetInfo
        )


class AccountGetProfileInfo(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self,) -> responses.account.GetProfileInfo:
        """ account.getProfileInfo
        From Vk Docs: Returns the current account info.
        Access from user token(s)
        
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request(
            "account.getProfileInfo",
            params,
            response_model=responses.account.GetProfileInfo,
        )


class AccountGetPushSettings(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, device_id: str) -> responses.account.GetPushSettings:
        """ account.getPushSettings
        From Vk Docs: Gets settings of push notifications.
        Access from user token(s)
        :param device_id: Unique device ID.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request(
            "account.getPushSettings",
            params,
            response_model=responses.account.GetPushSettings,
        )


class AccountRegisterDevice(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(
        self,
        token: str,
        device_model: str,
        device_year: int,
        device_id: str,
        system_version: str,
        settings: str,
        sandbox: bool,
    ) -> responses.account.RegisterDevice:
        """ account.registerDevice
        From Vk Docs: Subscribes an iOS/Android/Windows Phone-based device to receive push notifications
        Access from user token(s)
        :param token: Device token used to send notifications. (for mpns, the token shall be URL for sending of notifications)
        :param device_model: String name of device model.
        :param device_year: Device year.
        :param device_id: Unique device ID.
        :param system_version: String version of device operating system.
        :param settings: Push settings in a [vk.com/dev/push_settings|special format].
        :param sandbox: 
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request(
            "account.registerDevice",
            params,
            response_model=responses.account.RegisterDevice,
        )


class AccountSaveProfileInfo(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(
        self,
        first_name: str,
        last_name: str,
        maiden_name: str,
        screen_name: str,
        cancel_request_id: int,
        sex: int,
        relation: int,
        relation_partner_id: int,
        bdate: str,
        bdate_visibility: int,
        home_town: str,
        country_id: int,
        city_id: int,
        status: str,
    ) -> responses.account.SaveProfileInfo:
        """ account.saveProfileInfo
        From Vk Docs: Edits current profile info.
        Access from user token(s)
        :param first_name: User first name.
        :param last_name: User last name.
        :param maiden_name: User maiden name (female only)
        :param screen_name: User screen name.
        :param cancel_request_id: ID of the name change request to be canceled. If this parameter is sent, all the others are ignored.
        :param sex: User sex. Possible values: , * '1' – female,, * '2' – male.
        :param relation: User relationship status. Possible values: , * '1' – single,, * '2' – in a relationship,, * '3' – engaged,, * '4' – married,, * '5' – it's complicated,, * '6' – actively searching,, * '7' – in love,, * '0' – not specified.
        :param relation_partner_id: ID of the relationship partner.
        :param bdate: User birth date, format: DD.MM.YYYY.
        :param bdate_visibility: Birth date visibility. Returned values: , * '1' – show birth date,, * '2' – show only month and day,, * '0' – hide birth date.
        :param home_town: User home town.
        :param country_id: User country.
        :param city_id: User city.
        :param status: Status text.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request(
            "account.saveProfileInfo",
            params,
            response_model=responses.account.SaveProfileInfo,
        )


class AccountSetInfo(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, name: str, value: str) -> responses.account.SetInfo:
        """ account.setInfo
        From Vk Docs: Allows to edit the current account info.
        Access from user token(s)
        :param name: Setting name.
        :param value: Setting value.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request(
            "account.setInfo", params, response_model=responses.account.SetInfo
        )


class AccountSetNameInMenu(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(
        self, user_id: int, name: str
    ) -> responses.account.SetNameInMenu:
        """ account.setNameInMenu
        From Vk Docs: Sets an application screen name (up to 17 characters), that is shown to the user in the left menu.
        Access from user token(s)
        :param user_id: User ID.
        :param name: Application screen name.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request(
            "account.setNameInMenu",
            params,
            response_model=responses.account.SetNameInMenu,
        )


class AccountSetOffline(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self,) -> responses.account.SetOffline:
        """ account.setOffline
        From Vk Docs: Marks a current user as offline.
        Access from user token(s)
        
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request(
            "account.setOffline", params, response_model=responses.account.SetOffline
        )


class AccountSetOnline(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, voip: bool) -> responses.account.SetOnline:
        """ account.setOnline
        From Vk Docs: Marks the current user as online for 15 minutes.
        Access from user token(s)
        :param voip: '1' if videocalls are available for current device.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request(
            "account.setOnline", params, response_model=responses.account.SetOnline
        )


class AccountSetPushSettings(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(
        self, device_id: str, settings: str, key: str, value: typing.List
    ) -> responses.account.SetPushSettings:
        """ account.setPushSettings
        From Vk Docs: Change push settings.
        Access from user token(s)
        :param device_id: Unique device ID.
        :param settings: Push settings in a [vk.com/dev/push_settings|special format].
        :param key: Notification key.
        :param value: New value for the key in a [vk.com/dev/push_settings|special format].
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request(
            "account.setPushSettings",
            params,
            response_model=responses.account.SetPushSettings,
        )


class AccountSetSilenceMode(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(
        self, device_id: str, time: int, peer_id: int, sound: int
    ) -> responses.account.SetSilenceMode:
        """ account.setSilenceMode
        From Vk Docs: Mutes push notifications for the set period of time.
        Access from user token(s)
        :param device_id: Unique device ID.
        :param time: Time in seconds for what notifications should be disabled. '-1' to disable forever.
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'Chat ID', e.g. '2000000001'. For community: '- Community ID', e.g. '-12345'. "
        :param sound: '1' — to enable sound in this dialog, '0' — to disable sound. Only if 'peer_id' contains user or community ID.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request(
            "account.setSilenceMode",
            params,
            response_model=responses.account.SetSilenceMode,
        )


class AccountUnban(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, owner_id: int) -> responses.account.Unban:
        """ account.unban
        From Vk Docs: 
        Access from user token(s)
        :param owner_id: 
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request(
            "account.unban", params, response_model=responses.account.Unban
        )


class AccountUnregisterDevice(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(
        self, device_id: str, sandbox: bool
    ) -> responses.account.UnregisterDevice:
        """ account.unregisterDevice
        From Vk Docs: Unsubscribes a device from push notifications.
        Access from user token(s)
        :param device_id: Unique device ID.
        :param sandbox: 
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request(
            "account.unregisterDevice",
            params,
            response_model=responses.account.UnregisterDevice,
        )


class Account:
    def __init__(self, request):
        self.ban = AccountBan(request)
        self.change_password = AccountChangePassword(request)
        self.get_active_offers = AccountGetActiveOffers(request)
        self.get_app_permissions = AccountGetAppPermissions(request)
        self.get_banned = AccountGetBanned(request)
        self.get_counters = AccountGetCounters(request)
        self.get_info = AccountGetInfo(request)
        self.get_profile_info = AccountGetProfileInfo(request)
        self.get_push_settings = AccountGetPushSettings(request)
        self.register_device = AccountRegisterDevice(request)
        self.save_profile_info = AccountSaveProfileInfo(request)
        self.set_info = AccountSetInfo(request)
        self.set_name_in_menu = AccountSetNameInMenu(request)
        self.set_offline = AccountSetOffline(request)
        self.set_online = AccountSetOnline(request)
        self.set_push_settings = AccountSetPushSettings(request)
        self.set_silence_mode = AccountSetSilenceMode(request)
        self.unban = AccountUnban(request)
        self.unregister_device = AccountUnregisterDevice(request)
