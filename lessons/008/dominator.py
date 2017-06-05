#!/usr/bin/env python
# -*- coding: utf-8 -*-

# time O(n)
# space O(n)

import unittest
from util import Queue
from collections import defaultdict


"""
falta tratar caso em que número de elementos é ímpar
[0, 1, 0] deveria devolver 0 ou 2
"""

def solution_strange(A):
    n = len(A)
    if n == 1:
        return 0

    if n % 2 == 0:
        limit = n
    else:
        limit = n - 1
    pair = 0
    idx = -1
    for i in range(0, limit, 2):
        if A[i] == A[i+1]:
            pair += 1
            idx = i

    if pair == 0 and n % 2 == 0:
        return -1

    if idx == -1:
        idx = n - 1
    candidate = A[idx]

    c = 0
    for x in A:
        if x == candidate:
            c += 1

    if c > n / 2.:
        return idx
    else:
        return -1

def solution(A):
    n = len(A)

    if n == 0:
        return -1

    candidate = A[0]
    idx = 0
    count = 0
    for i, x in enumerate(A):
        if x == candidate:
            count += 1
        else:
            count -= 1
            if count == 0:
                idx = i
                candidate = x
                count += 1

    count = 0
    for x in A:
        if x == candidate:
            count += 1

    if count > n / 2.:
        return idx
    else:
        return -1




class Test(unittest.TestCase):
    def test(self):
        self.assertIn(solution([3, 4, 3, 2, 3, -1, 3, 3]), [0, 2, 4, 6, 7])

    def test2(self):
        self.assertEquals(-1, solution([3, 4, 3, 4]))
        self.assertEquals(-1, solution([1, 1, -2, -2]))
        self.assertEquals(-1, solution([1, -2]))
        self.assertEquals(-1, solution([-1, 2]))
        self.assertEquals(-1, solution([]))

    def test3(self):
        self.assertEquals(0, solution([-1]))
        self.assertEquals(0, solution([-2]))
        self.assertEquals(0, solution([0]))
        self.assertIn(solution([3, 3, 3, 3, 3]), range(5))
        self.assertIn(solution([3, 3, 3, 3, 3, 3, 3]), range(7))

    def test4(self):
        self.assertIn(solution([3, 3, 2, 3, 2]), [0, 1, 3])

    def test5(self):
        self.assertIn(solution([1, 1, 2, 2, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3]), range(8, 17))
        self.assertIn(solution([3, 2, 1, 2, 3, 2, 3, 3, 2, 3, 1, 3, 3, 3, 3, 1, 1]), [0, 4, 6, 7, 9, 11, 12, 13, 14])

    def test6(self):
        self.assertIn(solution([0, 1, 0]), [0, 2])

    def test7(self):
        self.assertIn(solution([0, 0, 0, 0, 0, 0, 1, 1]), range(6))

if __name__ == '__main__':
    unittest.main()
