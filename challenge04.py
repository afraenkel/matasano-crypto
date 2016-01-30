from __future__ import division
import utils

# ---------------------------------------------------------------------
# problem 4
# ---------------------------------------------------------------------

with open('data/prob4.txt') as data:
    scores = []
    for line in data:
        score, word, key = utils.test_single_char(line.strip().decode('hex'))
        scores.append((score, word, key))
    print max(scores)

