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


def recover_key(ciphertext):
    for x in range(10**6):
        cipher = mt_ctr(x)
        pt = cipher(ciphertext)
        if utils.ascii_score(pt) > 0.85:
            print "key: %d" % x
            print "plaintext: %s" % pt
            break

        
if __name__ == '__main__':
    enc_cipher = mt_ctr(KEY)
    string = 'A'*100
    ct = enc_cipher(string)
    recover_key(ct)
