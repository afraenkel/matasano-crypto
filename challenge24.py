import utils
import struct

KEY = 12345


def mt_ctr(key):
    mtgen = utils.mt(key)
    
    def closure(text):
        ct = ''
        for block in utils.get_blocks(text, 4):
            keyblock = struct.pack('I', mtgen.next())
            ct += utils.xor(keyblock, block)
        return ct

    return closure

if __name__ == '__main__':
    enc_cipher, dec_cipher = mt_ctr(KEY), mt_ctr(KEY)
    string = 'A'*100
    ct = enc_cipher(string)
    pt = dec_cipher(ct)
    print pt == string
