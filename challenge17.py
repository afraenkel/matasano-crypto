import utils
import random
from Crypto.Cipher import AES

cts = '''MDAwMDAwTm93IHRoYXQgdGhlIHBhcnR5IGlzIGp1bXBpbmc=
MDAwMDAxV2l0aCB0aGUgYmFzcyBraWNrZWQgaW4gYW5kIHRoZSBWZWdhJ3MgYXJlIHB1bXBpbic=
MDAwMDAyUXVpY2sgdG8gdGhlIHBvaW50LCB0byB0aGUgcG9pbnQsIG5vIGZha2luZw==
MDAwMDAzQ29va2luZyBNQydzIGxpa2UgYSBwb3VuZCBvZiBiYWNvbg==
MDAwMDA0QnVybmluZyAnZW0sIGlmIHlvdSBhaW4ndCBxdWljayBhbmQgbmltYmxl
MDAwMDA1SSBnbyBjcmF6eSB3aGVuIEkgaGVhciBhIGN5bWJhbA==
MDAwMDA2QW5kIGEgaGlnaCBoYXQgd2l0aCBhIHNvdXBlZCB1cCB0ZW1wbw==
MDAwMDA3SSdtIG9uIGEgcm9sbCwgaXQncyB0aW1lIHRvIGdvIHNvbG8=
MDAwMDA4b2xsaW4nIGluIG15IGZpdmUgcG9pbnQgb2g=
MDAwMDA5aXRoIG15IHJhZy10b3AgZG93biBzbyBteSBoYWlyIGNhbiBibG93'''
CT_LIST = map(lambda x: x.decode('base64'), cts.split('\n'))

KEY = utils.rand_bytes(16)


def enc_rand_ct():
    iv = utils.rand_bytes(16)
    pt = utils.pad(random.sample(CT_LIST, 1)[0])
    ct = AES.new(KEY, AES.MODE_CBC, iv).encrypt(pt)
    return ct, iv


def padding_oracle(ct, iv):
    pt = AES.new(KEY, AES.MODE_CBC, iv).decrypt(ct)
    try:
        utils.unpad(pt)
        return True
    except TypeError:
        return False

# To Do: implement the attack!


def attack():
    enc, iv = enc_rand_ct()
    block1, block2 = enc[0:16], enc[16:32]
    # f1 = changed byte block, i2 = intermediate block
    f1, i2 = bytearray('\x00'*16), bytearray('\x00'*16)
    
    # j = number of bytes from end of block
    # pad = padding byte at that point
    for j, pad in zip(range(16)[::-1], range(1, 17)):
        for char in range(0, 256):
            f1[j] = char
            if padding_oracle(bytes(f1 + block2), iv):
                break
        i2[j] = f1[j] ^ pad

        for k in range(j, 16):
            f1[k] = i2[k] ^ (pad + 1)

    p2 = utils.xor(block1, bytes(i2))
    print(p2)


if __name__ == '__main__':
    for _ in range(5):
        attack()
