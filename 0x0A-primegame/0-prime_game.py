#!/usr/bin/python3
"""Prime game module"""


def isWinner(x, nums):
    """Determine who is winner
    """

    if x <= 0 or nums is None:
        return None

    if x != len(nums):
        return None

    benCounts = 0
    mariaCounts = 0
    res = [1 for x in range(sorted(nums)[-1] + 1)]

    res[0], res[1] = 0, 0

    for i in range(2, len(res)):
        removeMultiples(res, i)

    for i in nums:
        if sum(res[0:i + 1]) % 2 == 0:
            benCounts += 1
        else:
            mariaCounts += 1
    if benCounts > mariaCounts:
        return "Ben"

    if mariaCounts > benCounts:
        return "Maria"

    return None


def removeMultiples(nums, num):
    """remove multiples"""
    for i in range(2, len(nums)):
        try:
            nums[i * num] = 0
        except (ValueError, IndexError):
            break
