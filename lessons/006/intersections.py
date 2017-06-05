#!/usr/bin/env python

# time O(n log n)
# space O(n)

import unittest

def solution_naive(A):
    n = len(A)
    c = 0
    for i, x in enumerate(A):
        for j in range(i+1, n):
            y = A[j]
            if i + x >= j - y:
                c += 1
    return c

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

def solution(A):
    l = []
    r = []
    for i, x in enumerate(A):
        r.append(A[i] + i)
        l.append(-1 * (A[i] - i))
        
    r = sorted(r)        
    l = sorted(l)

    n = len(A)
    spurious = (1 + n) * n / 2
    total = - spurious
    for rr in r:
        z = binary_search_le(l, rr) + 1
        total += z
        if total > 10000000:
            return -1

    return total


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(1, solution([1, 0]))

    def test1(self):
        self.assertEqual(11, solution([1, 5, 2, 1, 4, 0]))

    def test2(self):
        self.assertEqual(1, solution([1, 0]))

    def test3(self):
        self.assertEqual(3, solution([2, 0, 1]))

    def test4(self):
        self.assertEqual(3, solution([1, 1, 1]))

    def test5(self):
        self.assertEqual(1, solution([1, 0]))
        self.assertEqual(1, solution([0, 1]))
      
    def test_all_zeroes(self):
        self.assertEqual(0, solution([0, 0, 0, 0, 0]))

    def test_big(self):
        self.assertEqual(-1, solution([2147483647] * 10000000))


if __name__ == '__main__':
    unittest.main()
