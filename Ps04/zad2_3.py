import unittest

from lfsr import LFSR


def ssc(message, seed, mask):
    taps = []
    for index, item in enumerate(mask):
        if item == '1':
            taps.append(index)

    lfsr = LFSR(int(seed[::-1], 2), len(mask), taps)
    ret = 0

    for i in message:
        ret *= 2
        ret += int(i) ^ (lfsr.next()%2)

    return bin(ret)[2:]


def autokey(message, seed, mask, encode=True):
    taps = []
    for index, item in enumerate(mask):
        if item == '1':
            taps.append(index)

    lfsr = LFSR(int(seed[::-1], 2), len(mask), taps)
    ret = 0

    for i in message:
        bit = lfsr.get_xored_taps() ^ int(i)
        lfsr.next(bit if encode else int(i))
        ret *= 2
        ret += bit

    return bin(ret)[2:].zfill(len(message))


class StreamCyphersTests(unittest.TestCase):
    def test_ssc(self):
        self.assertEqual(ssc('11101001', '0010', '1001'), '10010011')
    

    def test_autokey(self):
        self.assertEqual(autokey('11101001', '0011', '1001', encode=True), '00110011')
        self.assertEqual(autokey('00110011', '0011', '1001', encode=False), '11101001')


if __name__ == "__main__":
    unittest.main()