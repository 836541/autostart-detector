# /undead_warlock
# GPL3.0-or-foward

import winreg
import os
import re 



class PersistenceObject:
    def __init__(self, key, subkey = None):
        self.key      = key 
        self.subkey   = subkey         
        self.name     = str()
        self.value    = str()
        self.datatype = int()
        self.path     = str() 
        self.loop     = 1
    
    def getValues(self):
        key  = winreg.OpenKey(self.key, self.subkey, reserved = 0, access = winreg.KEY_READ)
        if not key: 

            return 0                 # 0 if Fail 
        
        
        for index in range(0,100): 
            if self.loop:
                for index2 in range(0,3):
                    try:                    
                            keyvalues = winreg.EnumValue(key, index)[index2]   
                            if index2 == 0:
                                self.path  = keyvalues  
                                self.name  = re.findall(r"(\\(\w*\..*))", keyvalues)[0][1]
                            if index2 == 1: 
                                self.value = keyvalues  
                            if index2 == 2:
                                self.datatype = keyvalues              
                    except:
                            self.loop = 0
        
        return 1   # 1 if Success


def getdirFiles(dir, recursive):             # Startup Folders check
    files = list()
    if not recursive: 
        files = [os.listdir(dir)]
    
    if recursive:
        for (dirpath, dirnames, filenames) in os.walk(dir):
            files += [os.path.join(dirpath, file) for file in filenames]

    return files  


def getStartupFolders():
    folders = list() 
    regkeys = {"HKCU": winreg.HKEY_CURRENT_USER, "HKLM": winreg.HKEY_LOCAL_MACHINE } 
    HKCU_skeys = {
    "UserShellFolders": r"Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders",
    "ShellFolders"    : r"Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders"} 
    HKLM_skeys = {
    "ShellFolders"    : r"Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders",
    "UserShellFolders": r"Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders"}

    def registrySearch(key, subkeys, valuename):
        folders = list()
        for subkey in subkeys:
            try:
                openkey = winreg.OpenKey(key, subkey)
                for index in range(100):
                    keyvalue = winreg.EnumValue(openkey, index)
                    if keyvalue[0] == valuename:
                        folders += [keyvalue[1]]
                        break 
            except: 
                try:
                    continue
                except:
                    break  

        return folders

    for subkey in HKCU_skeys:
        folders +=  registrySearch(regkeys["HCKU"], subkey, "Startup")

    for subkey2 in HKLM_skeys: 
        folders += registrySearch(regkeys["HKLM"], subkey2, "Common Startup")

    ## Some folders will have % in the app, next step is using re to change this.








def main():
    regkeys = { "HKCU" : winreg.HKEY_CURRENT_USER, "HKLM" : winreg.HKEY_LOCAL_MACHINE } 
    hcku_subkeys = {"Run" : r"Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run"}

                         
                  




