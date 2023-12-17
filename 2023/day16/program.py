
import sys
import time

sys.setrecursionlimit(10000)

history = set()

def castBeamsRec(pos, dir, cave):

    y, x = pos

    if (pos, dir) in history:
        return 1
    
    if x < 0 or x >= len(cave[0]) or y < 0 or y >= len(cave):
        return 0
    
    history.add((pos, dir))
    
    match cave[x][y]:
        case "-":
            if dir in {(0, 1), (0, -1)}:
                return castBeamsRec((y, x), (1, 0), cave) + castBeamsRec((y, x), (-1, 0), cave)
        case "|":
            if dir in {(1, 0), (-1, 0)}:
                return castBeamsRec((y, x), (0, 1), cave) + castBeamsRec((y, x), (0, -1), cave)
        case "\\":
            newDir = (dir[1], dir[0])
            return castBeamsRec((y + newDir[0], x + newDir[1]), newDir, cave)
        case "/":
            newDir = (-dir[1], -dir[0])
            return castBeamsRec((y + newDir[0], x + newDir[1]), newDir, cave)
    
    return castBeamsRec((y + dir[0], x + dir[1]), dir, cave)

def solveRec(data):

    global history

    cave = tuple(["".join(row) for row in data])

    record = []

    for y in [0, len(cave) - 1]:

        for x in range(len(cave[y])):

            history = set()

            castBeamsRec((x, y), (0, 1 if y == 0 else -1), cave)

            energized = set()

            for pos, dir in history:

                energized.add(pos)
            
            record.append(len(energized))

    for y in range(len(cave)):

        for x in [0, len(cave[y]) - 1]:

            history = set()

            castBeamsRec((x, y), (1 if x == 0 else -1, 0), cave)

            energized = set()

            for pos, dir in history:

                energized.add(pos)
            
            record.append(len(energized))

    return max(record)

def main():

    data = []
    
    with open(sys.argv[1]) as f:

        for line in f:

            data.append(list(line.strip()))

    # result = solve(data)
    result = solveRec(data)

    print(result)

###########################

if __name__ == "__main__":
    startTime = time.time()
    main()
    print(f'Runtime {time.time() - startTime} sec')
