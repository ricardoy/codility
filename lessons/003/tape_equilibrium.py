#!/usr/bin/env python

import unittest

def solution(v):
    n = len(v)

    l = v[0]
    r = 0
    for i in range(1, n):
        r += v[i]

    min_diff = abs(l - r)

    # print 'a:', l, r

    for i in range(2, n):
        l += v[i-1]
        r -= v[i-1]
        diff = abs(l - r)
        # print l, r
        if diff < min_diff:
            min_diff = diff

    return min_diff


class Test(unittest.TestCase):
    def test(self):
        print 1111
        self.assertEqual(1, solution([3,1,2,4,3]))

    def test2(self):
        print 2222
        self.assertEqual(4, solution([3,-1]))

    def test3(self):
        self.assertEqual(0, solution([-1,-1]))

    def test4(self):
        self.assertEqual(4, solution([3,0,-1]))


    def test5(self):
        self.assertEqual(1, solution([3,-1, 1, 2]))

if __name__ == '__main__':
    unittest.main()
