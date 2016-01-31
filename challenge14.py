import random
from Crypto.Cipher import AES
import utils

KEY = utils.rand_bytes(16)
PREFIX = utils.rand_bytes(random.randint(0, 64))
MYST = open('data/prob12.txt').read().decode('base64')


def rand_encrypt(text):
    text = utils.pad(PREFIX + text + MYST, 16)
    return AES.new(KEY).encrypt(text)


def prefix_len():
    for k in range(32, 48):
        const = 'A'*k
        blocks = utils.get_blocks(rand_encrypt(const))
        for i, (x, y) in enumerate(zip(blocks, blocks[1:])):
            if x == y:
                return (16*(i-1) + (48 - k), i)


def find_plaintext():
    size = 512  # approx size of unknown text
    chars = map(chr, range(256))
    pt = ''
    prefix_length, block_span = prefix_len()
    padding = 16 - prefix_length % 16
    for i in range(1, size + 1):
        s = 'A' * (size - i + padding)
        ct = rand_encrypt(s)
        L = map(rand_encrypt, [s + pt + x for x in chars])
        for k, x in enumerate(L):
            start, end = 16*block_span, size + 16*block_span
            if x[start: end] == ct[start: end]:
                pt += chars[k]
                break
    return pt


if __name__ == '__main__':
    print find_plaintext()
