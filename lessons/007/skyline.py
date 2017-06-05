#!/usr/bin/env python

# time O(n)
# space O(1)

import unittest
from util import Queue

def solution(s):
    q = Queue(len(s))
    total = 0
    for token in s:
        if q.empty():
            q.put(token)
            total += 1
        else:
            if token > q.peek():
                q.put(token)
                total += 1
            else:
                while not q.empty() and token < q.peek():
                    q.get()
                if q.empty() or token != q.peek():
                    q.put(token)
                    total += 1
    return total

   
class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(7, solution([8, 8, 5, 7, 9, 8, 7, 4, 8]))        

    def test2(self):
        self.assertEqual(1, solution([1, 1]))
        self.assertEqual(2, solution([1, 1, 2]))
        self.assertEqual(2, solution([1, 2, 1]))
    
    def test3(self):
        self.assertEqual(3, solution([2, 1, 2]))

    def test_simple(self):
        self.assertEqual(1, solution([1]))
        self.assertEqual(1, solution([3]))

if __name__ == '__main__':
    unittest.main()


