#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n: int) -> int:
    """Description"""
    n = 'H'
    k = 'H'
    ans = 0
    while (len(k) < n):
        if n % len(k) == 0:
            ans += 2
            n = k
            k += k
        else:
            ans += 1
            k += n
    if len(k) != n:
        return 0
    return ans
