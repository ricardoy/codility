from math import log

import unittest
import sys


def solution(n):
    if n == 1:
        return 0

    bits = int(log(n, 2))
    best_gap = 0
    current_gap = 0
    one_found = False
    for i in range(bits, -1, -1):
        if n >= 2 ** i:
            n -= 2 ** i
            if one_found:
                best_gap = max(best_gap, current_gap)
                current_gap = 0
            one_found = True
        else:
            if one_found:
                current_gap += 1

    return best_gap


class BinaryGapTest(unittest.TestCase):

    def test9(self):
        self.assertEqual(2, solution(9))

    def test529(self):
        self.assertEqual(4, solution(529))

    def test_20(self):
        self.assertEqual(1, solution(20))

    def test_15(self):
        self.assertEqual(0, solution(15))

    def test_others(self):
        self.assertEqual(0, solution(1))
        self.assertEqual(0, solution(2))
        self.assertEqual(0, solution(3))
        self.assertEqual(0, solution(4))
        self.assertEqual(1, solution(5))

    def test_big(self):
        self.assertEqual(0, solution(2147483647))


if __name__ == '__main__':
    if len(sys.argv) == 1:
        unittest.main()
    else:
        print solution(int(sys.argv[1]))
