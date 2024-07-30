#!/usr/bin/python3

"""
N Queens solution
"""

import sys


def backtracking(x, h, columns, position, negative, board):
    """
    Backtracking
    """
    if x == h:
        res = []
        for l in range(len(board)):
            for k in range(len(board[l])):
                if board[l][k] == 1:
                    res.append([l, k])
        print(res)
        return

    for c in range(n):
        if c in columns or (x + c) in position or (x - c) in negative:
            continue

        columns.add(c)
        position.add(x + c)
        negative.add(x - c)
        board[x][c] = 1

        backtracking(x+1, h, columns, position, negative, board)

        columns.remove(c)
        position.remove(x + c)
        negative.remove(x - c)
        board[x][c] = 0


def nqueens(n):
    """
    N Queens solution
    """
    columns = set()
    pos = set()
    neg = set()
    board = [[0] * n for i in range(n)]

    backtrack(0, n, columns, pos, neg, board)


if __name__ == "__main__":
    num = sys.argv
    if len(num) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        nn = int(num[1])
        if nn < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens(nn)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
