from __future__ import division
import string

# ---------------------------------------------------------------------
# problem 6
# ---------------------------------------------------------------------

def hdist(s1, s2):
    ba1, ba2 = bytearray(s1), bytearray(s2)
    return sum(bin(i ^ j).count("1") for i, j in zip(ba1, ba2))


def pairwise_hdist(str_list):
    L = []
    for i, v in enumerate(str_list):
        for w in str_list[i+1:]:
            L.append(hdist(v, w))
    return sum(L)/len(str_list[0])


def keysize_distance(maxsize, text):
    D = {}
    for k in range(2, maxsize + 1):
        D[k] = pairwise_hdist(chunk_string(k, text))
    return D


def chunk_string(k, s):
    L = ['']*(len(s)//k + 1)
    for i, v in enumerate(s):
        L[i//k] += v
    return L[:-1]


def decrypt(keysize, s):
    for keychar in zip(*chunk_string(keysize, s)):
        # need to output the key in test_single_char!
        pass


# ---------------------------------------------------------------------


def test_single_char(s):
    testlist = range(256)
    byteslist = [''.join([chr(x ^ y) for x in bytearray(s)]) for y in testlist]
    for ba in byteslist:
        try:
            word = ba.encode('utf-8')
        except UnicodeDecodeError:
            return None
        if score_english(word):
            return word
    return None


def repeating_key_xor(key, s):
    key_arr, pt_arr = bytearray(key), bytearray(s)
    c = ''.join([chr(v ^ key_arr[k % len(key_arr)]) for k, v in enumerate(pt_arr)])
    return c


# English strings scoring function:

common_chars = ''.join([' ', ',', '.']) + string.ascii_letters


def score_english(s):
    l = len([c for c in s if c in common_chars])
    if l/len(s) > 0.9:
        return True
    else:
        return False
