#!/usr/bin/env python

import unittest


def solution(x, A):
    v = range(x + 1)
    for i in range(x + 1):
        v[i] = -1

    for i, y in enumerate(A):
        if v[y] < 0:
            v[y] = i

    if min(v[1:]) == -1:
        return -1
    else:
        return max(v[1:])



class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(6, solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))

    def test2(self):
        self.assertEqual(-1, solution(10, [1, 3, 1, 4, 2, 3, 5, 4]))

    def test3(self):
        self.assertEqual(0, solution(1, [1]))

    def test4(self):
        self.assertEqual(3, solution(3, [1, 2, 1, 3]))

    def test5(self):
        self.assertEqual(3, solution(2, [2, 2, 2, 1]))


if __name__ == '__main__':
    unittest.main()
