import utils
from Crypto.Cipher import AES

KEY = utils.rand_bytes(16)
PREFIX = "comment1=cooking%20MCs;userdata="
SUFFIX = ";comment2=%20like%20a%20pound%20of%20bacon"


def enc_user(text):
    text = utils.pad(text.replace(';', '').replace('=', ''))
    obj = AES.new(KEY, AES.MODE_CBC)
    return obj.encrypt(text)


def is_admin(ct):
    pt = AES.new(KEY, AES.MODE_CBC).decrypt(ct)
    return ";admin=true;" in pt


# ---------------------------------------------------------------------
# problem solution
# ---------------------------------------------------------------------
    
