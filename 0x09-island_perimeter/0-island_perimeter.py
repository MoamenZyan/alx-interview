#!/usr/bin/python3
"""My script"""


def island_perimeter(grid):
    """ return island perimeter
    """
    wi = len(grid[0])
    hi = len(grid)
    edge = 0
    siz = 0

    for i in range(hi):
        for j in range(wi):
            if grid[i][j] == 1:
                siz += 1
                if (j > 0 and grid[i][j - 1] == 1):
                    edge += 1
                if (i > 0 and grid[i - 1][j] == 1):
                    edge += 1
    return siz * 4 - edge * 2
