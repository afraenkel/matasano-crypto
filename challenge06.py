from __future__ import division
import utils


# ---------------------------------------------------------------------
# problem 6
# ---------------------------------------------------------------------

def pairwise_hdist(str_list):
    '''
    pairwise normalized hamming distance between
    equal length strings in a list.
    '''
    L = []
    for i, v in enumerate(str_list[:-1]):
        for w in str_list[i+1:]:
            L.append(utils.hdist(v, w))
    return sum(L)/(len(str_list[0])*len(str_list))


def keysize_distance(maxsize, text):
    '''
    '''
    D = {}
    for k in range(2, maxsize + 1):
        D[k] = pairwise_hdist(utils.get_blocks(text, k)[:4])
    return D


def decrypt_repeating_xor(ciphertext):
    keysize_probs = keysize_distance(42, ciphertext)
    keysizes = sorted(keysize_probs.items(), key=lambda x: x[1])

    for keysize, _ in keysizes:
        out, key = [], []
        for chunk in utils.blocked_zip(ciphertext, keysize):
            _, word, keychar = utils.test_single_char(chunk)
            out.append(word)
            key.append(keychar)

        chunk_length = len(out[0])
        out = [x + ' '*(chunk_length - len(x)) for x in out]
        plaintext = ''.join(map(lambda x: ''.join(x), zip(*out)))
        key = ''.join(key)

        if utils.ascii_score(plaintext) > 0.8:
            break
        else:
            print "keysize %d failed with score %f" % (keysize, utils.ascii_score(plaintext))

    return plaintext, key





with open('data/prob6.txt') as data:
    s = data.read().decode('base64')

    plaintext, key = decrypt_repeating_xor(s)

    print plaintext
    print key

