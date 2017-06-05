#!/usr/bin/env python

import unittest


def solution(v):
    hill = True
    valley = True
    last = v[0]
    total = 1
    for x in v:
        if last < x:
            if valley:
                total += 1
            hill = True
            valley = False
        elif last > x:
            if hill:
                total += 1
            hill = False
            valley = True

    return total

class Test(unittest.TestCase):
    def test(self):
        self.assertEquals(4, solution([2,2,3,4,3,3,2,2,1,1,2,5]))

    def test2(self):
        self.assertEquals(1, solution([1]))
        self.assertEquals(1, solution([-1000]))
        self.assertEquals(1, solution([1000]))

    def test3(self):
        self.assertEquals(1, solution([-1, -1]))
        self.assertEquals(1, solution([1, 1, 1]))

    def test4(self):
        self.assertEquals(2, solution([1, 2]))
        self.assertEquals(2, solution([2, 1]))
        self.assertEquals(2, solution([2, 1, 1, 1]))
        self.assertEquals(2, solution([1, 1, 1, 2, 2, 2]))

    def test5(self):
        self.assertEquals(2, solution([1, 2, 3, 4, 5]))
        self.assertEquals(2, solution([5, 4, 3, 2, 1]))

if __name__ == '__main__':
    unittest.main()
