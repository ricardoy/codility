#!/usr/bin/env python

import unittest

def solution(v):
    n = len(v)
    c = [0] * n

    for x in v:
        if x > 0 and x <= n:
            c[x - 1] += 1
        else:
            return 0

    for x in c:
        if x != 1:
            return 0
    return 1

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(1, solution([1]))

    def test2(self):
        self.assertEqual(0, solution([2]))

    def test3(self):
        self.assertEqual(1, solution([1, 2]))

    def test4(self):
        self.assertEqual(1, solution([1, 3, 2]))

    def test5(self):
        self.assertEqual(0, solution([6]))

if __name__ == '__main__':
    unittest.main()
