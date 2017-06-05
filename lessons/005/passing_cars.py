#!/usr/bin/env python

import unittest

def solution(A):
    n = len(A)
        
    west = 1
    for i in xrange(n-1, -1, -1):
        if A[i] == 1:
            A[i] = west
            west += 1

    east = -1
    for i in xrange(0, n):
        if A[i] == 0:
            A[i] = east
            east += -1

    i = 0
    j = 0
    total = 0
    while i < n and j < n:
        ri = i
        while ri < n and A[ri] < 0:
            ri += 1
        if ri >= n:
            break

        total += (ri - i) * A[ri]
        if total > 1000000000:
            total = -1
            break

        j = ri
        while j < n and A[j] > 0:
            j += 1
 
        i = j

    return total

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(5, solution([0, 1, 0, 1, 1]))

    def test2(self):
        self.assertEqual(6, solution([0, 0, 1, 1, 1]))

    def test3(self):
        self.assertEqual(0, solution([0]))
        self.assertEqual(0, solution([1]))

    def test4(self):
        self.assertEqual(0, solution([1, 0]))
        self.assertEqual(1, solution([0, 1]))
        self.assertEqual(2, solution([0, 1, 1]))
        self.assertEqual(2, solution([0, 1, 1, 0]))
        self.assertEqual(4, solution([0, 1, 1, 0, 1]))


if __name__ == '__main__':
    unittest.main()
