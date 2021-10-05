from pathlib import Path, PurePath
from comtypes import client
from comtypes.automation import VT_EMPTY

'''
Python IDM Helper by zackmark29
Version v1.1_2021.10.26
'''

class IDMHelper:
    def __init__(self,
                 url, output_folder, output_filename, flag,
                 #OPTIONALS
                 referer=None, cookies=None, post_data=None,
                 user_name=None, password=None, user_agent=None
                 ):
        ''' 
        flags
            0: Display/Pop-up confirmation before downloading
            1: Download automatically without any confirmations dialogs
            2: Display confirmation if found duplicate and add only to queue
            3: Add only to queue without any confirmation
        '''
        # common
        self.url = url
        self.flag = flag
        self.output_folder = output_folder
        self.output_filename = output_filename
                    
        # optionals
        self.referer = referer
        self.cookies = cookies
        self.post_data = post_data
        self.userName = user_name
        self.password = password
        self.user_agent = user_agent
        
        def check_folder(*dirs):
            for dir in dirs:
                if Path(dir).exists():
                    return dir
            raise NotADirectoryError("Looks like you don't have IDM installed in your system")

        # if you installed idm to another drive, just change the folder path
        
        idm_folder_64bit = 'C:\Program Files (x86)\Internet Download Manager'
        idm_folder_32bit = 'C:\Program Files\Internet Download Manager'

        idm_folder = check_folder(idm_folder_64bit, idm_folder_32bit)

        try:
            # Registry path: Computer\HKEY_CLASSES_ROOT\TypeLib\{ECF21EAB-3AA8-4355-82BE-F777990001DD}
            UUID = '{ECF21EAB-3AA8-4355-82BE-F777990001DD}'
            self.IDMan = client.GetModule([UUID, 1, 0])
        except OSError:
            # if uuid is not exist in the registry
            tlb = PurePath(idm_folder, 'idmantypeinfo.tlb')
            if not Path(tlb).is_file():
                raise FileNotFoundError(f'{tlb} is not exist. Try to re-install your idm')
                
            self.IDMan = client.GetModule(tlb)
            
    def send_to_IDM(self) -> None:
        idm = client.CreateObject(
            progid = 'IDMan.CIDMLinkTransmitter',
            interface = self.IDMan.ICIDMLinkTransmitter2
        )
        idm.SendLinkToIDM2(
            bstrUrl = self.url, 
            bstrReferer = self.referer, 
            bstrCookies = self.cookies, 
            bstrData = self.post_data, 
            bstrUser = self.userName, 
            bstrPassword = self.password, 
            bstrLocalPath = self.output_folder, 
            bstrLocalFileName = self.output_filename, 
            lFlags = self.flag,
            reserved1 = self.user_agent if self.user_agent is not None else VT_EMPTY,
            reserved2 = VT_EMPTY
        )

if __name__ == '__main__':
    url = 'http://www.internetdownloadmanager.com/idman401.exe'
    import os
    output_folder = os.getcwd()
    output_filename = 'idman.exe'
    user_agent = None
    flag = 3 #see above the flag information
    IDMHelper(url, output_folder, output_filename, flag, user_agent=user_agent).send_to_IDM()