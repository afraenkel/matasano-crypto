from __future__ import division
import utils

# ---------------------------------------------------------------------
# problem 2
# ---------------------------------------------------------------------


def xor(b1, b2):
    return [chr(x ^ y) for (x, y) in zip(b1, b2)]


s1 = '1c0111001f010100061a024b53535009181c'
s2 = '686974207468652062756c6c277320657965'
s3 = '746865206b696420646f6e277420706c6179'

ba = utils.xor(bytearray(s1.decode('hex')), bytearray(s2.decode('hex')))
print "problem 2 is solved: {0}".format(''.join(ba).encode('hex') == s3)

