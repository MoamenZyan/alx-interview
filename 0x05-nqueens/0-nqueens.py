#!/usr/bin/python3

import sys


def solution(row, column):
    sol = [[]]
    for queen in range(row):
        sol = queen_place(queen, column, sol)

    return solver


def queen_place(queen, column, pre_solve):
    queen_solver = []
    for arr in pre_solve:
        for h in range(column):
            if safe(queen, h, arr):
                queen_solver.append(arr + [h])

    return queen_solver


def safe(queen, h, arr):
    if h in arr:
        return (False)
    else:
        return all(abs(arr[column] - h) != queen - column
                   for column in range(queen))


def init():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit():
        queen = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)
    if queen < 4:
        print("N must be at least 4")
        sys.exit(1)

    return(queen)


def n_queens():
    queen = init()
    solver = solution(queen, queen)
    for arr in solver:
        clean = []
        for q, x in enumerate(arr):
            clean.append([q, x])
        print(clean)


if __name__ == '__main__':
    n_queens()
