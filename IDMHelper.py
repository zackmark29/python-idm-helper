from genericpath import isdir
import os
from os.path import join
from pathlib import Path
from comtypes import client
from comtypes.automation import VT_EMPTY

def dirExist(dir): return Path(dir).exists()

class IDMHelper:
    def __init__(self,
                 url,  outputFolderPath,  outputFileName, flag,
                 #OPTIONALS
                 referer=None, cookies=None, postData=None,
                 userName=None, password=None, userAgent=None
                 ):
        ''' 
        flags
            0: Display/Pop-up confirmation before downloading
            1: Download automatically without any confirmations dialogs
            2: Display confirmation if found duplicate and add only to queue
            3: Add only to queue without any confirmation
        '''
        #optionals
        self.referer    = referer
        self.cookies    = cookies
        self.postData   = postData
        self.userName   = userName
        self.password   = password
        self.userAgent  = userAgent
        
        self.url = url
        self.flag = flag
        self.outputFolderPath = outputFolderPath
        self.outputFileName = outputFileName
                    
        #if you installed idm to another drive, just change the folder path
        #since most of the system is 64bit and the default dir for 64bit is this
        idmPath = 'C:\Program Files (x86)\Internet Download Manager'
        if not dirExist(idmPath):
            idmPath = 'C:\Program Files\Internet Download Manager'
            if not dirExist(idmPath): #idm is not installed
                raise NotADirectoryError(idmPath)
        try:
             # Registry path: Computer\HKEY_CLASSES_ROOT\TypeLib\{ECF21EAB-3AA8-4355-82BE-F777990001DD}
            UUID = '{ECF21EAB-3AA8-4355-82BE-F777990001DD}'
            self.IDMan = client.GetModule([UUID, 1, 0])
        except:
            #if uuid is not exist in the registry
            tlb = join(idmPath, 'idmantypeinfo.tlb')
            if not Path(tlb).is_file():
                raise FileNotFoundError(f'{tlb} is not exist')
                
            self.IDMan = client.GetModule(tlb)
            
    def sendToIDM(self):
        client.CreateObject(
            progid='IDMan.CIDMLinkTransmitter', 
            interface=self.IDMan.ICIDMLinkTransmitter2).SendLinkToIDM2(
                self.url, 
                self.referer, 
                self.cookies, 
                self.postData, 
                self.userName, 
                self.password, 
                self.outputFolderPath, 
                self.outputFileName, 
                self.flag,
                self.userAgent if self.userAgent else VT_EMPTY,
                VT_EMPTY
            )

if __name__ == '__main__':
    url = 'http://www.internetdownloadmanager.com/idman401.exe'
    outputFolderPath = os.getcwd()
    outputFileName = 'idman.exe'
    customUserAgent = None
    flag = 3 #see above the flag information
    IDMHelper(url, outputFolderPath, outputFileName, flag, userAgent=customUserAgent).sendToIDM()