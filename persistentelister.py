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
        try:
            key  = winreg.OpenKey(self.key, self.subkey, reserved = 0, access = winreg.KEY_READ)
        except:
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

    

def main():
    regkeys = { "HKCU" : winreg.HKEY_CURRENT_USER, "HKLM" : winreg.HKEY_LOCAL_MACHINE } 
    subkeys = { "HKCU" : }
                         
                  




