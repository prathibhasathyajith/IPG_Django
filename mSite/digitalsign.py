import base64,binascii,OpenSSL
from OpenSSL import crypto


key_file = open("000000001000066.pem", "r")
key = key_file.read()
key_file.close()

# password = b'password'

# if key.startswith('-----BEGIN '):
# pkey = crypto.load_privatekey(crypto.FILETYPE_PEM, key, password)
pkey = crypto.load_privatekey(crypto.FILETYPE_PEM, key)
# pbkey = crypto.load_publickey(crypto.FILETYPE_PEM, key)

# else:
# pkey = crypto.load_pkcs12(key, password).get_privatekey()
data = b"000000001000066"
sign = OpenSSL.crypto.sign(pkey, data, "MD5")
# print(sign)

byteSignedDataString_lower = binascii.hexlify(sign)
byteSignedDataString_byte = byteSignedDataString_lower.upper()
byteSignedDataString = byteSignedDataString_byte.decode("utf-8")

#
# data_base64 = base64.b64encode(sign)
# print(data_base64)

print(byteSignedDataString);


## encrypt key 12093835
## B035BA39CCFD9E660C0033597C869237
