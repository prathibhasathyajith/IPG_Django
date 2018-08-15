from Cryptodome.PublicKey import RSA
from base64 import b64decode
import pem

certs = pem.parse_file("000000001000066.pem")

RSAPrivateKey = str(certs[0])


RSAPrivateKey_edit1 = RSAPrivateKey.strip()
RSAPrivateKey_edit2 = RSAPrivateKey_edit1.split('\n')
RSAPrivateKey_edit3 = [item.strip() for item in RSAPrivateKey_edit2]

del RSAPrivateKey_edit3[0]
del RSAPrivateKey_edit3[RSAPrivateKey_edit3.__len__()-1]

key = ''.join(RSAPrivateKey_edit3)
keyDER = b64decode(key)
keyPub = RSA.importKey(keyDER)

encrypt_key = int(str(keyPub.n)[:8])
print("modulus -- " + "" + str(encrypt_key))
print("{} -- {}".format("modulus", encrypt_key))