import utils

# ---------------------------------------------------------------------
# problem 9
# ---------------------------------------------------------------------

s1 = b"YELLOW SUBMARINE"
s2 = b"YELLOW SUBMARINE\x04\x04\x04\x04"

print "problem #9 is: {0}".format(utils.pad(s1, 20) == s2)
