#!/usr/bin/env python

# time O(n)
# space O(n)

import unittest
from util import Queue


def solution(S, D):
    assert(len(S) == len(D))
    q = Queue(len(S))

    total = 0
    for size, direction in zip(S, D):
        # print size, direction
        if direction == 1:
            q.put(size)
        else:
            if q.empty():
                total += 1
            else:
                while not q.empty():
                    upstream_size = q.get()
                    if upstream_size > size:
                        q.put(upstream_size)
                        break
                if q.empty():
                    total += 1

    # return total + q.size()
    return total + q.size()
   
class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(2, solution([4, 3, 2, 1, 5], [0, 1, 0, 0, 0]))

    def test2(self):
        self.assertEqual(3, solution([1, 2, 3], [0, 0, 0]))
        self.assertEqual(4, solution([1, 2, 3, 4], [0, 0, 0, 0]))
        self.assertEqual(5, solution([1, 2, 3, 4, 5], [0, 0, 0, 1, 1]))
        self.assertEqual(2, solution([1, 2, 3], [0, 1, 0]))
        self.assertEqual(1, solution([1, 2], [1, 0]))
        self.assertEqual(1, solution([1], [1]))
        self.assertEqual(1, solution([1], [0]))
        self.assertEqual(1, solution([2], [0]))
        self.assertEqual(1, solution([2], [1]))


if __name__ == '__main__':
    unittest.main()


