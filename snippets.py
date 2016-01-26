from __future__ import division
import string
import os
import random
from Crypto.Cipher import AES

def hdist(s1, s2):
    '''
    hamming distance between two strings s1 and s2
    '''
    ba1, ba2 = bytearray(s1), bytearray(s2)
    return sum(bin(i ^ j).count("1") for i, j in zip(ba1, ba2))


def pairwise_hdist(str_list):
    '''
    pairwise normalized hamming distance between
    equal length strings in a list.
    '''
    L = []
    for i, v in enumerate(str_list[:-1]):
        for w in str_list[i+1:]:
            L.append(hdist(v, w))
    return sum(L)/(len(str_list[0])*len(str_list))


def keysize_distance(maxsize, text):
    '''
    
    '''
    D = {}
    for k in range(2, maxsize + 1):
        D[k] = pairwise_hdist(chunk_string(k, text)[:4])
    return D


def chunk_string(k, s):
    '''
    chunk a string s into chunks of size k.
    '''
    L = ['']*(len(s)//k + 1)
    for i, v in enumerate(s):
        L[i//k] += v
    return L[:-1]


def chunk_and_zip(keysize, s):
    '''
    '''
    L = ['']*keysize
    for k, char in enumerate(s):
        L[k % keysize] += char
    return L


def test_single_char(s):
    testlist = range(128)
    byteslist = [''.join([chr(x ^ y) for x in bytearray(s)]) for y in testlist]
    outlist = []
    for k, ba in enumerate(byteslist):
        try:
            word = ba.encode('utf-8')
            outlist.append((ascii_score(word), word, k))
        except UnicodeDecodeError:
            outlist.append((0.0, '', k))

    score, word, k = max(outlist)
    return score, word, chr(k).encode('utf-8')


def repeating_key_xor(key, s):
    key_arr, pt_arr = bytearray(key), bytearray(s)
    c = ''.join([chr(v ^ key_arr[k % len(key_arr)]) for k, v in enumerate(pt_arr)])
    return c


def decrypt_repeating_xor(ciphertext):
    keysize_probs = keysize_distance(42, ciphertext)
    keysizes = sorted(keysize_probs.items(), key=lambda x: x[1])

    for keysize, _ in keysizes:
        out, key = [], []
        for chunk in chunk_and_zip(keysize, ciphertext):
            _, word, keychar = test_single_char(chunk)
            out.append(word)
            key.append(keychar)

        chunk_length = len(out[0])
        out = [x + ' '*(chunk_length - len(x)) for x in out]
        plaintext = ''.join(map(lambda x: ''.join(x), zip(*out)))
        key = ''.join(key)

        if ascii_score(plaintext) > 0.8:
            break
        else:
            print "keysize %d failed with score %f" %(keysize, ascii_score(plaintext))

    return plaintext, key

# ---------------------------------------------------------------------
# set2
# ---------------------------------------------------------------------


def padPKCS7(blocksize, plaintext):
    padnum = (blocksize - len(plaintext) % blocksize) % blocksize
    return plaintext + '\x04'*padnum


def cbc_encrypt(key, text):
    blocksize = len(key)
    text = padPKCS7(blocksize, text)
    iv = '\x00'*blocksize
    chunks = chunk_string(blocksize, text)

    obj = AES.new(key)
    ctext = [iv]
    for k, v in enumerate(chunks):
        z = zip(bytearray(v), bytearray(ctext[-1]))
        enc_block = obj.encrypt(''.join([chr(i ^ j) for (i, j) in z]))
        ctext.append(enc_block)

    return ''.join(ctext[1:])


def cbc_decrypt(key, text):
    blocksize = len(key)
    iv = '\x00'*blocksize
    chunks = chunk_string(blocksize, text)

    obj = AES.new(key)
    ptext = []
    while chunks:
        chunk = obj.decrypt(chunks.pop())
        try:
            prev_chunk = chunks[-1]
        except IndexError:
            prev_chunk = iv

        z = zip(bytearray(chunk), bytearray(prev_chunk))
        ptext.insert(0, ''.join([chr(i ^ j) for (i, j) in z]))
    
    return ''.join(ptext)


def rand_encrpyt(text, keysize=16):
    key = os.urandom(keysize)
    padding_size = random.randint(5, 10), random.randint(5, 10)
    pre_pad, post_pad = map(os.urandom, padding_size)
    text = sn.padPKCS7(keysize, pre_pad + text + post_pad)

    if random.random() < 0.5:
        # ECB mode
        return AES.new(key).encrypt(text), 'ECB'
    else:
        # CBC mode
        iv = os.urandom(keysize)
        return AES.new(key, mode=AES.MODE_CBC, IV=iv).encrypt(text), 'CBC'


def encryption_oracle(keysize, ciphertext):
    chunks = sn.chunk_string(keysize, ciphertext)
    if len(chunks) - len(set(chunks)) > 0:
        return 'ECB'
    else:
        return 'CBC'

# English strings scoring function:


def ascii_score(s):
    chars = string.ascii_letters + ' ,.-' + string.digits
    return sum([1 for x in s if x in chars])/len(s)
