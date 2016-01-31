import os
from Crypto.Cipher import AES
import utils

KEY = os.urandom(16)
MYST = open('data/prob12.txt').read().decode('base64')


def rand_encrypt(text):
    text = utils.pad(text + MYST, 16)
    return AES.new(KEY).encrypt(text)


def find_plaintext():
    size = 256  # approx size of unknown text
    chars = map(chr, range(256))
    pt = ''
    for i in range(1, size + 1):
        s = 'A'*(size-i)
        ct = rand_encrypt(s)
        L = map(rand_encrypt, [s + pt + x for x in chars])
        match = [k for k, x in enumerate(L) if x[:size] == ct[:size]]
        if len(match) == 1:
            pt += chars[match[0]]
        else:
            break
    print utils.unpad(pt)


if __name__ == '__main__':
    find_plaintext()    
