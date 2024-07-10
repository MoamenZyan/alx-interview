#!/usr/bin/python3
"""My Script."""


def minOperations(n):
    """Description."""
    if n < 2:
        return 0
    myList = []
    i = 1
    while n != 1:
        i += 1
        if n % i == 0:
            while n % i == 0:
                n /= i
                myList.append(i)
    return sum(myList)
