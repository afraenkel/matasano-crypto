import struct
import utils

KEY = 'YELLOW SUBMARINE'


def counter(blocknum):
    return struct.pack('<QQ', 0, blocknum)


if __name__ == '__main__':
    s = 'L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ=='
    s = s.decode('base64')

    print utils.ctr_crypto(s, KEY, counter)
