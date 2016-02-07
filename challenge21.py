import utils

mt_gen = utils.mt(1)

for _ in range(10):
    print mt_gen.next()
