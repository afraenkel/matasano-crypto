import snippets as sn


# ---------------------------------------------------------------------
# problem 9
# ---------------------------------------------------------------------

s1 = b"YELLOW SUBMARINE"
s2 = b"YELLOW SUBMARINE\x04\x04\x04\x04"

print "problem #9 is: {0}".format(sn.padPKCS7(20, s1) == s2)


# ---------------------------------------------------------------------
# problem 10
# ---------------------------------------------------------------------

plaintext = "hi my name is bob."
key = "YELLOW SUBMARINE"
ciphertext = sn.cbc_encrypt(key, plaintext)

ans = sn.cbc_decrypt(key, ciphertext).strip('\x04') == plaintext
print "problem #10 is: {0}".format(ans)

# ---------------------------------------------------------------------
# problem 11
# ---------------------------------------------------------------------

# import sample (large) text. run encrpyt / oracle

