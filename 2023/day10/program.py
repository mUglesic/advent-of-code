
import sys
import time

pipes = {
    "|": ((0, -1), (0, 1)),     # N-S
    "-": ((1, 0), (-1, 0)),     # E-W
    "L": ((0, -1), (1, 0)),     # N-E
    "J": ((0, -1), (-1, 0)),    # N-W
    "7": ((0, 1), (-1, 0)),     # S-W
    "F": ((0, 1), (1, 0)),      # S-E
}

mainPipe = []

def findStart(grid):

    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if c == "S":
                return (x, y)
            
def findConnection(grid, start):

    x, y = start

    # print(grid[y][x - 1], grid[y][x + 1], grid[y - 1][x], grid[y + 1][x])

    if grid[y][x - 1] in "-LF":
        return (x - 1, y)
    
    if grid[y][x + 1] in "-J7":
        return (x + 1, y)
    
    if grid[y - 1][x] in "|7F":
        return (x, y - 1)
    
    if grid[y + 1][x] in "|LJ":
        return (x, y + 1)
    
def findStartType(grid, start):

    x, y = start

    neighbors = set()

    if grid[y][x - 1] in "-LF":
        neighbors.add((-1, 0))
    
    if grid[y][x + 1] in "-J7":
        neighbors.add((1, 0))
    
    if grid[y - 1][x] in "|7F":
        neighbors.add((0, -1))
    
    if grid[y + 1][x] in "|LJ":
        neighbors.add((0, 1))

    for pipeType, pipeConnections in pipes.items():
        if neighbors == set(pipeConnections):
            return pipeType

def solve(data):

    xCurrent, yCurrent = findStart(data)

    mainPipe.append((xCurrent, yCurrent))

    xNext, yNext = findConnection(data, (xCurrent, yCurrent))

    xMove, yMove = (xNext - xCurrent, yNext - yCurrent)

    count = 1

    while data[yNext][xNext] != "S":

        mainPipe.append((xNext, yNext))

        if (xMove * -1, yMove * -1) == pipes[data[yNext][xNext]][0]:
            xMove, yMove = pipes[data[yNext][xNext]][1]
        else:
            xMove, yMove = pipes[data[yNext][xNext]][0]

        xCurrent, yCurrent = xNext, yNext

        xNext += xMove
        yNext += yMove

        count += 1

    return int(count / 2)

def solve2(data):

    xCurrent, yCurrent = findStart(data)

    data[yCurrent][xCurrent] = findStartType(data, (xCurrent, yCurrent))

    count = 0

    for y, line in enumerate(data):

        inside = False
        lastTurn = None

        for x, tile in enumerate(line):

            inMainPipe = (x, y) in mainPipe

            if inside:
                inside = not inMainPipe or not (tile == '|' or (lastTurn == "L" and tile == "7") or (lastTurn == "F" and tile == "J"))
            else:
                inside = inMainPipe and (tile == '|' or (lastTurn == "L" and tile == "7") or (lastTurn == "F" and tile == "J"))

            if inMainPipe and tile in "LJ7F":
                lastTurn = tile

            if inside and not inMainPipe:
                count += 1

    return count


def main():

    data = []
    
    with open(sys.argv[1]) as f:

        for line in f:

            data.append(list(line.strip()))

    result = solve(data)
    result2 = solve2(data)

    print(result, result2)


###########################

if __name__ == "__main__":
    startTime = time.time()
    main()
    print(f'Runtime {time.time() - startTime} sec')
