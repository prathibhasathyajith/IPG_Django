#libs

#cryptography
#pem
#pyOpenssl
#pycryptodomex

from keyset import keyProcess


f = keyProcess()
location = "storeSite/static/keyfile/000000001000066.pem"

print("{} -- {}".format("Byte Signed Data String",f.signingProcess(f.loadPemfile(location), "000000001000066")));
print("{}           -- {}".format("Encrypted mid", f.encryptionPrecess("000000001000066", f.generateSharedKey(location))))

