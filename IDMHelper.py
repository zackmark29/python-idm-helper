import os
from os.path import join
from os.path import isfile, isdir
import comtypes.client as cc
from comtypes.automation import VARIANT, VT_EMPTY

class IDMHelper:
    def __init__(self,
                 url,  outputFolderPath,  outputFileName, flag,
                 #OPTIONALS
                 referer=None, cookies=None, postData=None,
                 userName=None, password=None, userAgent=None
                 ):
        ''' 
        flag
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
        
        self.url = url
        self.flag = flag
        self.outputFolderPath = outputFolderPath
        self.outputFileName = outputFileName
        
        self.var1: VARIANT = VT_EMPTY if userAgent is None else userAgent
        self.var2: VARIANT = VT_EMPTY
                    
        #if you installed idm to another drive, just change the folder path
        x64 = 'C:\Program Files (x86)\Internet Download Manager' #64 bit
        x86 = 'C:\Program Files\Internet Download Manager'       #32 bit
        if not isdir(x64) or not isdir(x86):
            raise NotADirectoryError("IDM is not found. Please install first")
        try:
             # Registry path: Computer\HKEY_CLASSES_ROOT\TypeLib\{ECF21EAB-3AA8-4355-82BE-F777990001DD}
            UUID = '{ECF21EAB-3AA8-4355-82BE-F777990001DD}'
            self.IDMan = cc.GetModule([UUID, 1, 0])
        except:
            #if uuid is not exist in the registry
            idmFolder = x64 if isdir(x64) else x86
            tlb = join(idmFolder, 'idmantypeinfo.tlb')
            if not isfile(tlb):
                raise FileNotFoundError(f'{tlb} is not exist')
                
            self.IDMan = cc.GetModule(tlb)
            
    def sendToIDM(self):
        transmitter = cc.CreateObject('IDMan.CIDMLinkTransmitter', None, None, self.IDMan.ICIDMLinkTransmitter2)
        transmitter.SendLinkToIDM2(
            self.url, 
            self.referer, 
            self.cookies, 
            self.postData, 
            self.userName, 
            self.password, 
            self.outputFolderPath, 
            self.outputFileName, 
            self.flag,
            self.var1,
            self.var2
            )


if __name__ == '__main__':
    url = 'http://www.internetdownloadmanager.com/idman401.exe'
    outputFolderPath = os.getcwd()
    outputFileName = 'idman.exe'
    customUserAgent = None
    flag = 3 #see above the flag information
    IDMHelper(url, outputFolderPath, outputFileName, flag, userAgent=customUserAgent).sendToIDM()