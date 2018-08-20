import binascii, OpenSSL, pem
from OpenSSL import crypto
from Cryptodome.Util.Padding import pad
from Cryptodome.Cipher import DES
from Cryptodome.PublicKey import RSA
from base64 import b64decode


class keyProcess():

    def __init__(self):
        return

    # ---------------------digital signing-------------------

    def loadPemfile(self, location):
        key_file = open(location, "r")
        key = key_file.read()
        key_file.close()

        return key

    def signingProcess(self, key, mid):
        pkey = crypto.load_privatekey(crypto.FILETYPE_PEM, key)

        data = str.encode(mid)

        sign = OpenSSL.crypto.sign(pkey, data, "MD5")

        byteSignedDataString_lower = binascii.hexlify(sign)
        byteSignedDataString_byte = byteSignedDataString_lower.upper()
        byteSignedDataString = byteSignedDataString_byte.decode(" utf-8")

        return str(byteSignedDataString);

    # --------------------------------------------------------

    # --------------symantic encryption-----------------------

    # modulus generate process
    def generateSharedKey(self, location):
        certs = pem.parse_file(location)

        RSAPrivateKey = str(certs[0])

        RSAPrivateKey_edit1 = RSAPrivateKey.strip()
        RSAPrivateKey_edit2 = RSAPrivateKey_edit1.split('\n')
        RSAPrivateKey_edit3 = [item.strip() for item in RSAPrivateKey_edit2]

        del RSAPrivateKey_edit3[0]
        del RSAPrivateKey_edit3[RSAPrivateKey_edit3.__len__() - 1]

        key = ''.join(RSAPrivateKey_edit3)
        keyDER = b64decode(key)
        keyPub = RSA.importKey(keyDER)

        encrypt_key = int(str(keyPub.n)[:8])
        sharedKey = str(encrypt_key);

        return sharedKey;

    # encryption process
    def encryptionPrecess(self, mid, sharedkey):
        key = str.encode(sharedkey)

        cipher = DES.new(key, DES.MODE_ECB)

        MID = str.encode(mid)

        BLOCK_SIZE = 16

        msg = cipher.encrypt(pad(MID, BLOCK_SIZE))
        msg2 = binascii.hexlify(msg)
        msg3 = msg2.decode("utf-8")
        encryptedmid = msg3.upper()

        return str(encryptedmid)

    # --------------------------------------------------------
