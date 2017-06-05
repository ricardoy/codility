import unittest
import sys


def solution(v):
    r = 0
    for i in v:
        r = r ^ i

    return r


class SolutionTest(unittest.TestCase):

    def test(self):
        self.assertEqual(7, solution([9, 3, 9, 3, 9, 7, 9]))

    def test_single_value(self):
        self.assertEqual(1, solution([1]))
        self.assertEqual(2, solution([2]))
        self.assertEqual(3, solution([3]))
        self.assertEqual(1000, solution([1000]))

    def test2(self):
        self.assertEqual(1, solution([1, 10, 10]))

    def test3(self):
        self.assertEqual(9, solution([1, 1, 9, 1, 1]))


if __name__ == '__main__':
    if len(sys.argv) == 1:
        unittest.main()
    else:
        print solution(int(sys.argv[1]))
