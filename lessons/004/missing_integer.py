#!/usr/bin/env python

# check this http://www.geeksforgeeks.org/find-duplicates-in-on-time-and-constant-extra-space/

import unittest

# def solution(A):
#     c = set()
#
#     for i in [x for x in A if x > 0]:
#         c.add(i)
#
#     for i in xrange(1, 2147483648):
#         if i not in c:
#             return i

def solution(A):
    A = [x for x in A if x > 0]
    size = len(A)

    for i in xrange(0, size):
        # if abs(A[i]) - 1 < size and A[abs(A[i]) - 1] > 0:
        if abs(A[i]) - 1 < size and A[abs(A[i]) - 1] > 0:
            A[abs(A[i]) - 1] = -A[abs(A[i]) - 1]

    for i in xrange(0, size):
        if A[i] > 0:
            return i+1

    # print 222222222222
    return size+1


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(5, solution([1,3,6,4,1,2]))

    def test2(self):
        self.assertEqual(7, solution([1,3,6,4,1,2,5]))

    def test3(self):
        self.assertEqual(1, solution([6,5,4,3,2]))

    def test4(self):
        self.assertEqual(7, solution([6,5,4,3,2,10,1]))

    def test5(self):
        self.assertEqual(1, solution([-10, -20, -30, -2]))

    def test6(self):
        self.assertEqual(1, solution([-1, 0]))

    def test7(self):
        self.assertEqual(1, solution([0]))

    def test8(self):
        self.assertEqual(2, solution([546478784512123, 1231456787874, 5454689787, 1]))

    def test_dim_1(self):
        self.assertEqual(1, solution([4]))
        self.assertEqual(1, solution([2]))
        self.assertEqual(2, solution([1]))



if __name__ == '__main__':
    unittest.main()
