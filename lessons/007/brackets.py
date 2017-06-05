#!/usr/bin/env python

# time O(n)
# space O(n)

import unittest
from util import Queue

# def solution(s):
#     q = Queue.LifoQueue()
#     for token in s:
#         if token in '{[(':
#             q.put(token)
#         else:
#             if q.qsize() == 0:
#                 return 0
#             if token == ')':
#                 if q.get() != '(':
#                     return 0
#             elif token == '}':
#                 if q.get() != '{':
#                     return 0
#             else:
#                 if q.get() != '[':
#                     return 0

#     if q.qsize() == 0:
#         return 1
#     else:
#         return 0

def solution(s):
    q = Queue(len(s))
    for token in s:
        if token in '{[(':
            q.put(token)
        else:
            if q.empty():
                return 0
            if token == ')':
                if q.get() != '(':
                    return 0
            elif token == '}':
                if q.get() != '{':
                    return 0
            else:
                if q.get() != '[':
                    return 0

    if q.empty():
        return 1
    else:
        return 0

   
class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(1, solution('()'))

    def test1(self):
        self.assertEqual(1, solution(''))
        self.assertEqual(1, solution('()'))
        self.assertEqual(1, solution('[]'))
        self.assertEqual(1, solution('{}'))
        self.assertEqual(1, solution('{[()()]}'))
        
    def test0(self):
        self.assertEqual(0, solution('([)()]'))
        self.assertEqual(0, solution('([)()]{'))
        self.assertEqual(0, solution('(((((([[{{{[[[[[(((('))


if __name__ == '__main__':
    unittest.main()


