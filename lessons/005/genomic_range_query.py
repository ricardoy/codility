#!/usr/bin/env python

import unittest

# a = 1
# c = 2
# g = 3
# t = 4

def solution(s, p, q):
    n = len(s)
    a = [0] * (n + 1)
    c = [0] * (n + 1)
    g = [0] * (n + 1)
    t = [0] * (n + 1)

    aa = 0
    cc = 0
    gg = 0
    tt = 0

    for i, x in enumerate(s):
        if x == 'A':
            aa += 1
        elif x == 'C':
            cc += 1
        elif x == 'G':
            gg += 1
        else:
            tt += 1
        i += 1
        a[i] = aa
        c[i] = cc
        g[i] = gg
        t[i] = tt

    result = []
    for l, r in zip(p, q):
        r = r + 1
        if a[r] != a[l]:
            result.append(1)
        elif c[r] != c[l]:
            result.append(2)
        elif g[r] != g[l]:
            result.append(3)
        else:
            result.append(4)

    return result

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual([2, 4, 1], solution('CAGCCTA', [2, 5, 0], [4, 5, 6]))

    def test2(self):
        self.assertEqual([1, 2, 4], solution('ACGT', [0, 1, 3], [3, 1, 3]))

    def test3(self):
        self.assertEqual([1, 2, 3, 4], solution('ACGT', [0, 1, 2, 3], [0, 1, 2, 3]))
        self.assertEqual([4, 3, 2, 1], solution('ACGT', [3, 2, 1, 0], [3, 2, 1, 0]))

if __name__ == '__main__':
    unittest.main()
