#!/usr/bin/python3
""" My script """


def makeChange(coins, total):
    """ Script
    """

    if total <= 0:
        return 0
    chk = 0
    tmp = 0
    coins.sort(reverse=True)
    for i in coins:
        while chk < total:
            chk += i
            tmp += 1
        if chk == total:
            return tmp
        chk -= i
        tmp -= 1
    return -1
