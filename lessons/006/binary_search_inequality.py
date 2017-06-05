#!/usr/bin/env python

import unittest

def solution(A, x):
    return binary_search_le(A, x)

def binary_search_le(A, x):
    '''Returns the maximum value of i | A[i] <= x'''
    l = 0
    r = len(A) - 1    
    k = -1

    while l <= r:
        k = (l + r) / 2
        item = A[k]
        if item == x:
            r = k
            break
        if x > item:
            l = k + 1
        else:
            r = k - 1

    while True:
        if r + 1 < len(A):
            if A[r + 1] == x:
                r += 1
                continue            
        break

    return r

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(-1, solution([0, 1, 2, 3, 4], -1))
        self.assertEqual(0, solution([0, 1, 2, 3, 4], 0))
        self.assertEqual(1, solution([0, 1, 2, 3, 4], 1))
        self.assertEqual(2, solution([0, 1, 2, 3, 4], 2))
        self.assertEqual(4, solution([0, 1, 2, 3, 4], 4))
        self.assertEqual(4, solution([0, 1, 2, 3, 4], 10))
        self.assertEqual(2, solution([0, 1, 2, 4], 3))

    def test2(self):
        self.assertEqual(5, solution([1, 1, 1, 1, 1, 1], 1))

    
if __name__ == '__main__':
    unittest.main()


