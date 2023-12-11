
import sys
import time

import numpy as np

pipes = {
    "|": ((0, -1), (0, 1)),     # N-S
    "-": ((1, 0), (-1, 0)),     # E-W
    "L": ((0, -1), (1, 0)),     # N-E
    "J": ((0, -1), (-1, 0)),    # N-W
    "7": ((0, 1), (-1, 0)),     # S-W
    "F": ((0, 1), (1, 0)),      # S-E
}

def findStart(grid):

    for i, line in enumerate(grid):
        for j, c in enumerate(line):
            if c == "S":
                return (i, j)
            
def findConnection(grid, start):

    x, y = start

    # print(grid[x - 1][y], grid[x + 1][y], grid[x][y - 1], grid[x][y + 1])

    if grid[x - 1][y] == "-" or grid[x - 1][y] == "L" or grid[x - 1][y] == "F":
        return (x - 1, y)
    
    if grid[x + 1][y] == "-" or grid[x + 1][y] == "J" or grid[x + 1][y] == "7":
        return (x + 1, y)
    
    if grid[x][y - 1] == "|" or grid[x][y - 1] == "7" or grid[x][y - 1] == "F":
        return (x, y - 1)
    
    if grid[x][y + 1] == "|" or grid[x][y + 1] == "L" or grid[x][y + 1] == "J":
        return (x, y + 1)

def solve(data):

    grid = ["".join([data[j][i] for j in range(len(data))]) for i in range(len(data[0]))]

    # print(data, grid, sep="\n")

    xCurrent, yCurrent = findStart(grid)

    xNext, yNext = findConnection(grid, (xCurrent, yCurrent))

    xMove, yMove = (xNext - xCurrent, yNext - yCurrent)

    count = 1

    while grid[xNext][yNext] != "S":

        if (xMove * -1, yMove * -1) == pipes[grid[xNext][yNext]][0]:
            xMove, yMove = pipes[grid[xNext][yNext]][1]
        else:
            xMove, yMove = pipes[grid[xNext][yNext]][0]

        xCurrent, yCurrent = xNext, yNext

        xNext += xMove
        yNext += yMove

        count += 1

    return int(count / 2)   

def main():

    data = []
    
    with open(sys.argv[1]) as f:

        for line in f:

            data.append(line.strip())

    result = solve(data)

    print(result)


###########################

if __name__ == "__main__":
    startTime = time.time()
    main()
    print(f'Runtime {time.time() - startTime} sec')
