#!/usr/bin/env python

# time O(n log n)
# space O(n)

import unittest

def solution(A):
    neg = sorted([-1 * x for x in A if x < 0])
    pos = sorted([x for x in A if x >= 0])

    if len(neg) == 0:
        return pos[-1] * pos[-2] * pos[-3]
    else:
        if len(neg) == 1:
            if len(pos) < 3:
                return neg[0] * pos[0] * pos[1] * -1
            else:
                return pos[-1] * pos[-2] * pos[-3]
        else:
            if len(pos) > 2:
                return max(pos[-1] * neg[-1] * neg[-2],
                           pos[-1] * pos[-2] * neg[-1] * -1,
                           pos[-1] * pos[-2] * pos[-3])
            elif len(pos) > 1:
                return max(pos[-1] * neg[-1] * neg[-2],
                           pos[-1] * pos[-2] * neg[-1] * -1)
            elif len(pos) > 0:
                return pos[-1] * neg[-1] * neg[-2]
            else:
                return -1 * neg[0] * neg[1] * neg[2]
   
    return 0

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(60, solution([-3, 1, 2, -2, 5, 6]))
        self.assertEqual(24, solution([1, 2, 3, 4]))
        self.assertEqual(-12, solution([-1, 3, 4]))
        self.assertEqual(24, solution([-1, 2, 3, 4]))

    def test2(self):
        self.assertEqual(900, solution([-10, -30, 1, 2, 3]))

    def test3(self):
        self.assertEqual(0, solution([0, 1, 2]))

    def test4(self):
        self.assertEqual(0, solution([0, 1, 2, -1]))
        self.assertEqual(6, solution([0, 1, 2, -1, -3]))

    def test5(self):
        self.assertEqual(-6, solution([-10, -3, -2, -1]))

    def test6(self):
        self.assertEqual(32, solution([4, 4, 2, 0]))
        self.assertEqual(4, solution([-1, -2, 2, 0]))
        self.assertEqual(0, solution([-1, -2, 0]))
        self.assertEqual(2, solution([-1, -2, 1]))
    
if __name__ == '__main__':
    unittest.main()


