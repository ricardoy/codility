#!/usr/bin/env python

import unittest

def solution(n):
    i = 0
    while i ** 2 < n:
        i += 1

    best = 0
    current = 0
    found_one = False
    for i in range(i, -1, -1):
        if 2 ** i <= n:
            found_one = True
            n = n - 2 ** i
            if current > best:
                best = current
            current = 0
        else:
            if found_one:
                current += 1
    return best

class Test(unittest.TestCase):
    def test1041(self):
        self.assertEqual(5, solution(1041))

    def test9(self):
        self.assertEqual(2, solution(9))

    def test529(self):
        self.assertEqual(4, solution(529))

    def test20(self):
        self.assertEqual(1, solution(20))

    def test15(self):
        self.assertEqual(0, solution(15))

    def test2(self):
        self.assertEqual(0, solution(2))

    def test5(self):
        self.assertEqual(1, solution(5))

    def test6(self):
        self.assertEqual(0, solution(6))

    def test0(self):
        self.assertEqual(0, solution(0))

if __name__ == '__main__':
    unittest.main()
