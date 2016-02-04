import utils

PT = [x.decode('base64') for x in open('data/prob20.txt')]

KEY = utils.rand_bytes(16)
NONCE = lambda x: '\x00'*16

CT = map(lambda x: utils.ctr_crypto(x, KEY, NONCE), PT)


def zipblc(L):
    flattened = ['']*16
    for s in L:
        for k, char in enumerate(s):
            flattened[k % 16] += char
    return flattened

        
def decrypt_fixed_nonce(ciphertexts):
    keystream = ''.join([utils.test_single_char(x)[2] for x in zipblc(ciphertexts)])
    out = []
    for s in ciphertexts:
        pt = ''
        for k in range(len(s)//16 + 1):
            pt += utils.xor(keystream, s[16*k:16*(k+1)])
        out.append(pt)
    return '\n'.join(out), keystream
            



if __name__ == '__main__':
    text, keystream = decrypt_fixed_nonce(CT)
    print "plaintext:\n\n %s\n" % text
    print "keystream:\n\n %s" % repr(keystream)
