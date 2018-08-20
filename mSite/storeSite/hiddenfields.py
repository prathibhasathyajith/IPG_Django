import os


class xAllfields():

    def getmid(self):
        files = os.listdir('storeSite/static/keyfile/');
        mid = "" ;
        for keyfile in files:
            if keyfile.split(".")[1] == "pem":
                mid = keyfile.split(".")[0]
                break
            print(keyfile)

        return mid;


