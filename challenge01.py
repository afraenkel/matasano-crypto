from __future__ import division


# ---------------------------------------------------------------------
# problem 1
# ---------------------------------------------------------------------


def hex2b64(s):
    return s.decode('hex').encode('base64').strip()

s1 = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
s2 = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

print "problem 1 is solved: {0}".format(hex2b64(s1) == s2)
