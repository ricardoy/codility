#!/usr/bin/env python

# time O(n)
# space O(1)

import unittest

def solution(s):
    c = 0
    for t in s:
        if t == '(':
            c += 1
        else:
            if c == 0:
                return 0
            else:
                c -= 1
    if c == 0:
        return 1
    else:
        return 0

   
class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(1, solution('()'))
        self.assertEqual(1, solution('(())'))
        self.assertEqual(1, solution('(()())'))
        self.assertEqual(1, solution('(()()(()(()())))'))
        self.assertEqual(1, solution('()(())'))
        self.assertEqual(1, solution('()(())'))

    def test1(self):
        self.assertEqual(0, solution('('))
        self.assertEqual(0, solution(')'))
        self.assertEqual(0, solution('())'))
        self.assertEqual(0, solution('(()()()()(()()()()()()())))'))
        



if __name__ == '__main__':
    unittest.main()


