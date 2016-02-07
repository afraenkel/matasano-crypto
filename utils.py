from __future__ import division
import string
import os


def rand_bytes(size):
    return os.urandom(size)


def hdist(s1, s2):
    '''hamming distance between two strings s1 and s2'''
    ba1, ba2 = bytearray(s1), bytearray(s2)
    return sum(bin(i ^ j).count("1") for i, j in zip(ba1, ba2))


def get_blocks(s, k=16):
    '''chunk a string s into chunks of size k.'''
    L = ['']*(len(s)//k + 1)
    for i, v in enumerate(s):
        L[i//k] += v
    return L[:-1]


def blocked_zip(s, keysize=16):
    '''
    returns a list of strings whose jth entry is a
    string composed of the jth bytes in each block.
    '''
    L = ['']*keysize
    for k, char in enumerate(s):
        L[k % keysize] += char
    return L


def pad(plaintext, blocksize=16):
    padnum = (blocksize - len(plaintext) % blocksize)
    return plaintext + chr(padnum)*padnum


def unpad(plaintext, blocksize=16):
    pad = plaintext[-1]
    pad_length = ord(pad)
    if sum([x != pad for x in plaintext[-pad_length:]]) > 0:
        raise TypeError("invalid padding")
    else:
        return plaintext[:-pad_length]


def num_dupes(L):
    return len(L) - len(set(L))

# ---------------------------------------------------------------------
# hand-rolled encryption functions
# ---------------------------------------------------------------------


def repeating_key_xor(key, s):
    repkey = key*(len(s)//len(key)) + key[:len(s) % len(key)]
    return xor(repkey, s)


def cbc_cryto(text, key, iv, mode='MODE_ENCRYPT'):
    bs = len(key)
    if mode == 'MODE_ENCRYPT':
        text = pad(text, bs)
    blocks = get_blocks(text, bs)

    from Crypto.Cipher import AES
    obj = AES.new(key)

    if mode == 'MODE_ENCRYPT':
        ctext = [iv]
        for v in blocks:
            ctext.append(obj.encrypt(xor(v, ctext[-1])))
        return ''.join(ctext[1:])

    elif mode == 'MODE_DECRYPT':
        ptext = []
        while blocks:
            block = obj.decrypt(blocks.pop())
            try:
                prev_block = blocks[-1]
            except IndexError:
                prev_block = iv
            ptext.insert(0, xor(block, prev_block))
        return ''.join(ptext)


def ctr_crypto(text, key, nonce):
    from Crypto.Cipher import AES
    obj = AES.new(key)
    keystream = lambda x: obj.encrypt(nonce(x))
    
    pt = ''
    for k in range(len(text)//16 + 1):
        block = text[16*k:16*(k+1)]
        pt += xor(keystream(k), block)
    return pt


# ---------------------------------------------------------------------
# RNGs
# ---------------------------------------------------------------------


def mt(seed=4357):

    N, M = 624, 397
    A, UMASK, LMASK = 0x9908b0df, 0x80000000, 0x7fffffff
    TMASKB, TMASKC, MASK32 = 0x9d2c5680, 0xefc60000, 0xffffffff

    TSHIFTU = lambda y: (y >> 11)
    TSHIFTS = lambda y: (y << 7)
    TSHIFTT = lambda y: (y << 15)
    TSHIFTL = lambda y: (y >> 18)
    
    state = [seed & MASK32]
    for n in range(1, N):
        state.append(69069 * state[-1] & MASK32)

    i = -1
    while True:
        i = (i + 1) % N

        y = (state[i] & UMASK) | (state[(i+1) % N] & LMASK)
        state[i] = state[(i+M) % N] ^ (y >> 1)
        if y & 0x1:
            state[i] ^= A

        n = state[i]
        n ^= TSHIFTU(n)
        n ^= TSHIFTS(n) & TMASKB
        n ^= TSHIFTT(n) & TMASKC
        n ^= TSHIFTL(n)

        yield n


# ---------------------------------------------------------------------
# XOR functions
# ---------------------------------------------------------------------

def xor(s1, s2):
    '''
    xor of two byte strings s1 and s2. Truncates to
    min length of s1 and s2.
    '''
    z = zip(bytearray(s1), bytearray(s2))
    return ''.join([chr(i ^ j) for (i, j) in z])


def test_single_char(s):
    byteslist = [xor(s, y*len(s)) for y in map(chr, range(256))]
    outlist = []
    for k, ba in enumerate(byteslist):
        try:
            word = ba.encode('utf-8')
            outlist.append((ascii_score(word), word, k))
        except UnicodeDecodeError:
            outlist.append((0.0, '', k))

    score, word, k = max(outlist)
    return score, word, chr(k)


# ---------------------------------------------------------------------
# English strings scoring function:
# ---------------------------------------------------------------------

def ascii_score(s):
    chars = string.ascii_letters + ' ,.-' + string.digits
    return sum([1 for x in s if x in chars])/len(s)
