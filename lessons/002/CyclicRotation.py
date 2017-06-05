#!/usr/bin/env python

import unittest

def solution(v, k):
    n = len(v)
    if n == 0:
        return v
    k = k % n

    return v[n - k:] + v[0: n - k]

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual([9, 7, 6, 3, 8], solution([3, 8, 9, 7, 6], 3))

    def test2(self):
        self.assertEqual([], solution([], 3))

    def test3(self):
        self.assertEqual([3, 8, 9, 6], solution([3, 8, 9, 6], 0))

    def test4(self):
        self.assertEqual([1], solution([1], 1))

    def test5(self):
        self.assertEqual([1], solution([1], 0))

    def test6(self):
        self.assertEqual([1, 2], solution([1, 2], 0))
        self.assertEqual([2, 1], solution([1, 2], 1))
        self.assertEqual([1, 2], solution([1, 2], 2))
        self.assertEqual([2, 1], solution([1, 2], 3))
        self.assertEqual([1, 2], solution([1, 2], 4))

if __name__ == '__main__':
    unittest.main()
