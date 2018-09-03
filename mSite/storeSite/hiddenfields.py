import os
from .keyset import keyProcess


class Allfields():

    def getmid(self):
        files = os.listdir('storeSite/static/keyfile/');
        for keyfile in files:
            if keyfile.split(".")[1] == "pem":
                mid = keyfile.split(".")[0]
                break
            print(keyfile)

        return mid;

    def getemid(self,mid,location):
        sec = keyProcess()
        emid = sec.encryptionPrecess(mid, sec.generateSharedKey(location))
        return emid;

    def getbytesigneddatastring(self,mid,location):
        sec = keyProcess()
        bytesigneddatastring = sec.signingProcess(sec.loadPemfile(location), mid)
        return bytesigneddatastring;
