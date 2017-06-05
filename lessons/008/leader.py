#!/usr/bin/env python

# time O(n)
# space O(n)

import unittest
from collections import defaultdict


# def solution(A):
#     n = len(A)
#     size = 0
#     for k in xrange(n):
#         if (size == 0):
#             size += 1
#             value = A[k]
#         else:
#             if value != A[k]:
#                 size -= 1
#             else:
#                 size += 1
#     candidate = -1
#
#     if size > 0:
#         candidate = value
#     leader = None
#     count = 0
#     for k in xrange(n):
#         if A[k] == candidate:
#             count += 1
#     if count > n // 2:
#         leader = candidate
#     return leader


def solution(A):
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


class Test(unittest.TestCase):
    def test(self):
        self.assertEquals((4, 4), solution([4, 3, 4, 4, 4, 2]))
        self.assertEquals((1, 2), solution([1, 2, 1]))
        self.assertEquals((None, 0), solution([1, 2, 1, 2]))

    def test2(self):
        self.assertEquals((1, 2), solution([1, 1]))
        self.assertEquals((1, 3), solution([1, 2 ,1, 1]))
        self.assertEquals((1, 10), solution([2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
        self.assertEquals((2, 6), solution([2, 2, 2, 2, 2, 2, 1, 1, 1]))


if __name__ == '__main__':
    unittest.main()


