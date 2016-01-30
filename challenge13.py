from Crypto.Cipher import AES
import utils

KEY = utils.rand_bytes(16)
CRYPTO = AES.new(KEY)

# ---------------------------------------------------------------------
# problem set-up functions
# ---------------------------------------------------------------------


def decode_cookie(s):
    return dict(map(lambda x: x.split('='), s.split('&')))


def encode_cookie(d):
    L = ['='.join((k, d[k])) for k in ['email', 'uid', 'role']]
    return '&'.join(L)


def profile_for(user):
    user = user.replace('=', '').replace('&', '')
    return {'email': user, 'uid': '10', 'role': 'user'}


def encrypt_user_profile(s):
    return CRYPTO.encrypt(utils.pad(s, 16))


def decrypt_and_parse(s):
    encoded_cookie = utils.unpad(CRYPTO.decrypt(s))
    return decode_cookie(encoded_cookie)


def enc_profile(user):
    return encrypt_user_profile(encode_cookie(profile_for(user)))


# ---------------------------------------------------------------------
# problem solution functions
# ---------------------------------------------------------------------


user = 'amf@gmail.admin\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0bcom'
ct = enc_profile(user)
moved = ct[0:16] + ct[32:48] + ct[16:32]
print(decrypt_and_parse(moved))
