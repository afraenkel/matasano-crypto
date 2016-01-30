from __future__ import division
import utils

# ---------------------------------------------------------------------
# problem 3
# ---------------------------------------------------------------------


s1 = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

_, word, key = utils.test_single_char(s1.decode('hex'))

print "key is {0}\nplaintext is {1}".format(key, word)
