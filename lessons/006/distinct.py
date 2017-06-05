#!/usr/bin/env python


def solution(A):
    d = set()
    for x in A:
        d.add(x)
    return len(d)