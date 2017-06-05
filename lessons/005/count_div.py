#!/usr/bin/env python

import unittest
from math import ceil

def solution(a, b, k):
    k = float(k)
    l = ceil(a / k) * k
    r = int(b / k) * k

    if l > b:
        return 0

    return int(1 + ((r - l) / k))


class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(3, solution(6, 11, 2))

    def test2(self):
        self.assertEqual(1, solution(0, 0, 3))

    def test3(self):
        self.assertEqual(0, solution(1, 1, 3))

    def test4(self):
        self.assertEqual(2, solution(0, 5, 5))

    def test5(self):
        self.assertEqual(6, solution(10, 20, 2))

if __name__ == '__main__':
    unittest.main()
