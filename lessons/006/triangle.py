#!/usr/bin/env python

# time O(n log n)
# space O(n)

import unittest

def solution(A):
    A = sorted(A)
    n = len(A)

    for i in range(0, n - 2):
        if A[i] + A[i+1] > A[i+2]:
            return 1

    return 0
   

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(1, solution([10, 2, 5, 1, 8, 20]))

    def test2(self):
        self.assertEqual(0, solution([0, 1, 2]))

    def test3(self):
        self.assertEqual(0, solution([0, 0, 0, 0]))

    def test4(self):
        self.assertEqual(0, solution([1, 2, 3]))

    def test5(self):
        self.assertEqual(1, solution([2, 2, 3]))

    def test6(self):
        self.assertEqual(0, solution([10, 50, 5, 1]))

    def test7(self):
        self.assertEqual(0, solution([]))
        self.assertEqual(0, solution([1]))
        self.assertEqual(0, solution([1, 2]))


if __name__ == '__main__':
    unittest.main()
