#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


# slow, max_count should not be applied for the whole vector
# def solution(n, A):
#     v = [0] * n
#     max_found = 0
#     for k in A:
#         if k == n + 1:
#             v = [max_found] * n
            
#         else:
#             v[k-1] += 1
#             if v[k-1] > max_found:
#                 max_found = v[k-1]

#     return v

def solution(n, A):
    v = [0] * n
    max_found = 0
    max_count_applied = 0

    for k in A:
        k = k - 1
        if k == n:
            max_count_applied = max_found
            pass
        else:
            v[k] = 1 + max(v[k], max_count_applied)
            if v[k] > max_found:
                max_found = v[k]
    for i, x in enumerate(v):
        v[i] = max(max_count_applied, x)

    return v

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual([3, 2, 2, 4, 2], solution(5, [3, 4, 4, 6, 1, 4, 4]))    

    def test2(self):
        self.assertEqual([0, 0, 1, 0, 0], solution(5, [3]))

    def test3(self):
        self.assertEqual([0, 0, 0, 0, 0], solution(5, [6]))

    def test4(self):
        self.assertEqual([1], solution(1, [1, 2]))

    def test5(self):
        self.assertEqual([2], solution(1, [1, 2, 1, 2]))

    def test6(self):
        self.assertEqual([1, 1], solution(2, [1, 2]))

    def test7(self):
        self.assertEqual([2, 2], solution(2, [1, 1, 3, 3, 3]))


if __name__ == '__main__':
    unittest.main()
