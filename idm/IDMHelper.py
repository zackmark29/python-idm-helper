"""
Python IDM Helper by zackmark29
Edited by iAliF
Version v1.0.3 | 2023.05.14
"""

from typing import Optional

from comtypes import client
from comtypes.automation import VT_EMPTY

from module import get_module


class IDMHelper:
    def __init__(self) -> None:
        self._idm_module = get_module()
        self._idm = client.CreateObject(
            progid='IDMan.CIDMLinkTransmitter',
            interface=self._idm_module.ICIDMLinkTransmitter2
        )

    def send_link_to_idm(
            self,
            url: str,
            output_folder: str,
            output_file_name: str,
            flag: int,
            referer: Optional[str] = None,
            cookies: Optional[str] = None,
            post_data: Optional[str] = None,
            user_name: Optional[str] = None,
            password: Optional[str] = None,
            user_agent: Optional[str] = None
    ) -> None:
        """
        Send link to idm

        @param url: Url to download
        @param output_folder: Output folder
        @param output_file_name: Output file name
        @param flag:
            0: Display/Pop-up confirmation before downloading
            1: Download automatically without any confirmations dialogs
            2: Display confirmation if found duplicate and add only to queue
            3: Add only to queue without any confirmation
        @param referer: Referer
        @param cookies: Cookies
        @param post_data: PostData (if using POST method)
        @param user_name: Username
        @param password: Password
        @param user_agent: User-agent
        """
        self._idm.SendLinkToIDM2(
            bstrUrl=url,
            bstrReferer=referer,
            bstrCookies=cookies,
            bstrData=post_data,
            bstrUser=user_name,
            bstrPassword=password,
            bstrLocalPath=output_folder,
            bstrLocalFileName=output_file_name,
            lFlags=flag,
            reserved1=user_agent if user_agent else VT_EMPTY,
            reserved2=VT_EMPTY
        )
