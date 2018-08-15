from Cryptodome.Util.Padding import pad
import binascii
from Cryptodome.Cipher import DES

key = b'12093835'
cipher = DES.new(key, DES.MODE_ECB)
plaintext = b'000000001000066'
BLOCK_SIZE = 16
msg = cipher.encrypt(pad(plaintext,BLOCK_SIZE))
print(msg)

msg2 = binascii.hexlify(msg)
msg3 = msg2.decode("utf-8")
msg4 = msg3.upper()

print(msg4)