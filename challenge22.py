import utils
import time
import random


"""
Write a routine that performs the following operation:

Wait a random number of seconds between, I don't know, 40 and 1000.
Seeds the RNG with the current Unix timestamp
Waits a random number of seconds again.
Returns the first 32 bit output of the RNG.
You get the idea. Go get coffee while it runs. Or just simulate the passage of time, although you're missing some of the fun of this exercise if you do that.

From the 32 bit RNG output, discover the seed.
"""


def generate_number():
    time.sleep(random.randint(40, 1000))
    seed = int(time.time())
    mtgen = utils.mt(seed)
    time.sleep(random.randint(0, 30))
    return seed, mtgen.next()


def get_seed(num):
    start = int(time.time())
    while start > 0:
        if utils.mt(start).next() == num:
            return start
        else:
            start -= 1
    raise StopIteration("couldn't find seed")


if __name__ == '__main__':
    seed, num = generate_number()
    try:
        seed_guess = get_seed(num)
    except StopIteration:
        print "FAIL. SEED NOT FOUND"
    if seed == seed_guess:
        print "seed guessed correctly!"
    else:
        print "FAIL. Incorrect guess"
