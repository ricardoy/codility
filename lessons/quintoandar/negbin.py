#!/usr/bin/env python

import unittest


def input_to_number(v):
    r = 0
    for i, x in enumerate(v):
        r += (x * ((-2) ** i))

    return r


def solution(v):
    n = len(v)

    acc = 0
    for i in xrange(n-2, -1, -2):
        acc += (-2) ** i

    x = input_to_number(v)
    objective = -1 * x

    if objective == 0:
        return []
    elif objective > 0:
        if objective > acc:
            most_significant_bit_idx = n
        else:
            most_significant_bit_idx = n - 2
    else:
        if objective < acc:
            most_significant_bit_idx = n
        else:
            most_significant_bit_idx = n - 2

    limit_sum = [0 for _ in range(most_significant_bit_idx+1)]
    current_sum = 0
    for i in xrange(0, most_significant_bit_idx+1, 2):
        current_sum += (-2) ** i
        limit_sum[i] = current_sum

    current_sum = 0
    for i in xrange(1, most_significant_bit_idx+1, 2):
        current_sum += (-2) ** i
        limit_sum[i] = current_sum

    # print limit_sum

    result = [0 for _ in range(most_significant_bit_idx+1)]
    result[most_significant_bit_idx] = 1

    # print result

    current = (-2) ** most_significant_bit_idx
    # print current
    for i in xrange(most_significant_bit_idx-1, -1, -1):
        power = (-2) ** i
        dif = objective - current
        used = 0
        if dif > 0:
            if dif > get_limit_strictly_less(i, limit_sum) and power > 0:
                used = 1
        elif dif < 0:
            if dif < get_limit_strictly_less(i, limit_sum) and power < 0:
                used = 1
        else:
            used = 0

        if used:
            result[i] = 1
            current += power
        else:
            result[i] = 0

    return result


def get_limit_strictly_less(i, limit_sum):
    if i-2 < 0:
        return 0
    else:
        return limit_sum[i-2]


class Test(unittest.TestCase):
    def test(self):
        self.assertEquals([1, 1, 0, 1], solution([1, 0, 0, 1, 1])) # x = 9

    def test2(self):
        self.assertEquals([1, 1, 0, 1, 0, 1, 1], solution([1, 0, 0, 1, 1, 1])) # x = -23

    def test3(self):
        self.assertEquals([], solution([]))

    def test4(self):
        self.assertEquals([0, 1, 1], solution([0, 1])) # x = -2


if __name__ == '__main__':
    unittest.main()
