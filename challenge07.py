from __future__ import division


# ---------------------------------------------------------------------
# problem 7
# ---------------------------------------------------------------------

# AES-128 in ECB mode
from Crypto.Cipher import AES

key = "YELLOW SUBMARINE"
obj = AES.new(key)

with open('data/prob7.txt') as data:
    print obj.decrypt(data.read().decode('base64'))
