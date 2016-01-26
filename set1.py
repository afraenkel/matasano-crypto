from __future__ import division
import snippets as sn

# ---------------------------------------------------------------------
# problem 1
# ---------------------------------------------------------------------


def hex2b64(s):
    return s.decode('hex').encode('base64').strip()

s1 = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
s2 = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

print "problem 1 is solved: {0}".format(hex2b64(s1) == s2)

# ---------------------------------------------------------------------
# problem 2
# ---------------------------------------------------------------------


def xor(b1, b2):
    return [chr(x ^ y) for (x, y) in zip(b1, b2)]


s1 = '1c0111001f010100061a024b53535009181c'
s2 = '686974207468652062756c6c277320657965'
s3 = '746865206b696420646f6e277420706c6179'

ba = xor(bytearray(s1.decode('hex')), bytearray(s2.decode('hex')))
print "problem 2 is solved: {0}".format(''.join(ba).encode('hex') == s3)

# ---------------------------------------------------------------------
# problem 3
# ---------------------------------------------------------------------

s1 = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

print sn.test_single_char(s1.decode('hex'))

# ---------------------------------------------------------------------
# problem 4
# ---------------------------------------------------------------------

with open('data/prob4.txt') as data:
    scores = []
    for line in data:
        score, word, key = sn.test_single_char(line.strip().decode('hex'))
        scores.append((score, word, key))
    print max(scores)


# ---------------------------------------------------------------------
# problem 5
# ---------------------------------------------------------------------

pt = '''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''

ct = '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'

result = sn.repeating_key_xor('ICE', pt)

print "problem 5 is solved: {0}".format(result == ct.decode('hex'))

# ---------------------------------------------------------------------
# problem 6
# ---------------------------------------------------------------------

with open('data/prob6.txt') as data:
    s = data.read().decode('base64')

    plaintext, key = sn.decrypt_repeating_xor(s)

    print plaintext
    print key

# ---------------------------------------------------------------------
# problem 7
# ---------------------------------------------------------------------

# AES-128 in ECB mode
from Crypto.Cipher import AES

key = "YELLOW SUBMARINE"
obj = AES.new(key)

with open('data/prob7.txt') as data:
    print obj.decrypt(data.read().decode('base64'))

# ---------------------------------------------------------------------
# problem 8
# ---------------------------------------------------------------------

M = [x for x in open('data/prob8.txt')]
for i, x in enumerate(M):
    s = len(sn.chunk_string(16, x)) - len(set(sn.chunk_string(16, x)))
    if s > 0:
        print i
