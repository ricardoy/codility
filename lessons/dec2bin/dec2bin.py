#!/usr/bin/env python

# time O(n)
# space O(n)

import unittest


def solution(n):
    b = ''
    i = 0
    while True:
        r = n % 2
        b = str(r) + b
        n = n / 2
        if n == 0:
            break

    return b


class Test(unittest.TestCase):
    def test(self):
        self.assertEquals('0', solution(0))
        self.assertEquals('1', solution(1))
        self.assertEquals('10', solution(2))
        self.assertEquals('100', solution(4))
        self.assertEquals('101', solution(5))


if __name__ == '__main__':
    unittest.main()
