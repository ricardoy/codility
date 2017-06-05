#!/usr/bin/env python

import unittest

def solution(v):
    actual = 0
    for x in v:
        actual += x

    n = len(v)

    expected = ((1 + (n + 1)) * (n + 1)) / 2

    return expected - actual



class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(5, solution([1, 2, 3, 4, 6]))

    def test2(self):
        self.assertEqual(6, solution([1, 2, 3, 4, 5]))

    def test3(self):
        self.assertEqual(2, solution([1]))
        self.assertEqual(1, solution([2]))


if __name__ == '__main__':
    unittest.main()
