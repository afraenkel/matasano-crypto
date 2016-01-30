import utils
import random
from Crypto.Cipher import AES


def rand_encrpyt(text, keysize=16):
    key = utils.rand_bytes(keysize)
    padding_size = random.randint(5, 10), random.randint(5, 10)
    pre_pad, post_pad = map(utils.rand_bytes, padding_size)
    text = utils.pad(pre_pad + text + post_pad, keysize)

    if random.random() < 0.5:
        # ECB mode
        return AES.new(key).encrypt(text), 'ECB'
    else:
        # CBC mode
        iv = utils.rand_bytes(keysize)
        return AES.new(key, mode=AES.MODE_CBC, IV=iv).encrypt(text), 'CBC'


def encryption_oracle(ciphertext, keysize):
    chunks = utils.get_blocks(ciphertext, keysize)
    if utils.num_dupes(chunks) > 0:
        return 'ECB'
    else:
        return 'CBC'


if __name__ == '__main__':
    text = open('/usr/share/info/sieve').read().strip()
    for _ in range(10):
        ct, ans = rand_encrpyt(text, 16)
        print encryption_oracle(ct, 16) == ans
        
