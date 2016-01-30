from __future__ import division
import utils


# ---------------------------------------------------------------------
# problem 8
# ---------------------------------------------------------------------

M = [x for x in open('data/prob8.txt')]
for i, x in enumerate(M):
    b = utils.get_blocks(x, 16)
    if utils.num_dupes(b) > 0:
        print "ECB encrypted line is on line {0}".format(i)
