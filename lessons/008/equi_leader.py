#!/usr/bin/env python

# time O(n)
# space O(n)

import unittest
from collections import defaultdict


def leader(A):
    d = dict()
    k = 0
    number = None
    for x in A:
        if x not in d:
            d[x] = 1
        else:
            d[x] += 1

        if d[x] > k:
            k = d[x]
            number = x

    n = len(A)
    if k > n // 2:
        return number, k
    else:
        return None, 0


def solution(A):
    (l, c) = leader(A)
    if l is None:
        return 0

    n = len(A)
    lc = 0
    rc = c
    result = 0
    for i in xrange(n):
        if A[i] == l:
            lc += 1
            rc -= 1
        if lc > (i + 1) / 2 and rc > (n - i - 1) / 2:
            result += 1
    return result


class Test(unittest.TestCase):
    def test(self):
        self.assertEquals(2, solution([4, 3, 4, 4, 4, 2]))
        self.assertEquals(0, solution([1, 2, 1]))
        self.assertEquals(0, solution([1, 2, 1, 2]))

    def test2(self):
        self.assertEquals(1, solution([1, 1]))
        self.assertEquals(2, solution([1, 2 ,1, 1]))

    def test3(self):
        self.assertEquals(0, solution([1, 2, 1, 2, 1, 2, 1, 2]))


if __name__ == '__main__':
    unittest.main()


