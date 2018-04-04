import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256

def hash(message):
    hashV = SHA256.new()
    hashV.update(message)
    return hashV.digest()

class AESCipher(object):

    def __init__(self, key):
        self.bs = len(key)
        self.key = key

    def encrypt(self, raw):
        # raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        obj = AES.new(self.key, AES.MODE_CBC, iv)
        cipher = obj.encrypt(raw)
        # res = base64.b64decode(iv+cipher)
        return iv+hash(raw)+cipher

    def decrypt(self, enc):
        # enc = base64.b64decode(enc)
        # print(len(enc))
        iv = enc[:AES.block_size]
        hashRaw = enc[AES.block_size:48]
        # print(len(iv))
        obj = AES.new(self.key, AES.MODE_CBC, iv)
        # print(len(enc[AES.block_size:]))
        decrypt = obj.decrypt(enc[48:])
        hashC = hash(decrypt)
        if hashC == hashRaw:
        # return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')
            return decrypt
        else:
            return 0

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]
