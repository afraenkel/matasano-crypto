import utils


# ---------------------------------------------------------------------
# problem 10
# ---------------------------------------------------------------------

plaintext = "hi my name is bob."
key = "YELLOW SUBMARINE"
ciphertext = utils.cbc_cryto(plaintext, key, '\x00'*16)

pt = utils.cbc_cryto(ciphertext, key, '\x00'*16, 'MODE_DECRYPT')
pt = utils.unpad(pt)

print plaintext
print pt
print "problem #10 is: {0}".format(pt == plaintext)
