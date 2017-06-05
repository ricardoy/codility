#!/usr/bin/env python

# tempo O(n)
# mem O(n)

import unittest

def solution(A):    
    n = len(A)
    
    c = 0
    v = []
    v.append(0) # guardian
    for x in A:
        c += x
        v.append(c)
  
    best = 100000000
    best_i = -1
    best_j = -1
    for i in range(1, n+1):
        for j in range(i+1, i+3):
            if j > n:
                continue
            avg = (v[j] - v[i-1]) / float(j - i + 1)
            if avg < best:
                best = avg
                best_i = i
                best_j = j
                
    # return (best, best_i, best_j)
    return best_i - 1

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(1, solution([4, 2, 2, 5, 1, 5, 8]))

    def test2(self):
        self.assertEqual(0, solution([-10000, 10000, 2, 5, 1, 5, 8]))

    def test3(self):
        self.assertEqual(0, solution([0, 0, 0, 0]))

    def test4(self):
        self.assertEqual(2, solution([0, 1, -1, 0]))



if __name__ == '__main__':
    unittest.main()
