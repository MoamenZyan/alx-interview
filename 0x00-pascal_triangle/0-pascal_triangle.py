#!/usr/bin/python3
"""
first algorithm
"""


def pascal_triangle(n):
    """
    Returns a array of integers
    """
    ans = []
    if n <= 0:
        return ans
    ans = [[1]]
    for i in range(1, n):
        temp = [1]
        for j in range(len(ans[i - 1]) - 1):
            curr = ans[i - 1]
            temp.append(ans[i - 1][j] + ans[i - 1][j + 1])
        temp.append(1)
        ans.append(temp)
    return ans
