from utils import unpad


def test_unpad_exception(arg):
    try:
        unpad(arg)
    except TypeError:
        return True
    return False


if __name__ == '__main__':
    r1 = "ICE ICE BABY\x04\x04\x04\x04"
    s1 = "ICE ICE BABY"

    r2 = "ICE ICE BABY\x05\x05\x05\x05"
    r3 = "ICE ICE BABY\x01\x02\x03\x04"

    print "unpadding works: {0}".format(unpad(r1) == s1)
    print "handles wrong byte: {0}".format(test_unpad_exception(r2))
    print "handles different bytes: {0}".format(test_unpad_exception(r3))
