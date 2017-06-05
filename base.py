#!/usr/bin/env python

import unittest

def solution(n):
    pass

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(5, solution(1))

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())


if __name__ == '__main__':
    unittest.main()
