import utils
from Crypto.Cipher import AES

KEY = utils.rand_bytes(16)
IV = '\x00'*16
PREFIX = "comment1=cooking%20MCs;userdata="
SUFFIX = ";comment2=%20like%20a%20pound%20of%20bacon"


def enc_user(text):
    text = PREFIX + text.replace(';', '').replace('=', '') + SUFFIX
    obj = AES.new(KEY, mode=AES.MODE_CBC, IV=IV)
    return obj.encrypt(utils.pad(text))


def is_admin(ct):
    pt = AES.new(KEY, mode=AES.MODE_CBC, IV=IV).decrypt(ct)
    return ";admin=true;" in pt


# ---------------------------------------------------------------------
# problem solution
# ---------------------------------------------------------------------


if __name__ == '__main__':
    #      '0123456789ABCDEF0123456789ABCDEF'
    user = '000000000000000000000:admin+true'

    # flip bytes 5 and 11 in block 3 with ; and =

    ba = bytearray(enc_user(user))
    pos_sc = len(PREFIX) + 5
    pos_eq = len(PREFIX) + 11

    ba[pos_sc] = ba[pos_sc] ^ ord(';') ^ ord(':')
    ba[pos_eq] = ba[pos_eq] ^ ord('=') ^ ord('+')

    print "admin=True is found: {0}".format(is_admin(bytes(ba)))
