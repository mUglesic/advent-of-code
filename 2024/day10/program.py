
import sys
import time

def findTrailheads(m):

    trailheads = []

    for i, line in enumerate(m):
        for j, el in enumerate(line):
            if el == 0:
                trailheads.append((i, j))
    
    return trailheads

def findPath(m, i, j, s, pv):

    if i < 0 or i >= len(m) or j < 0 or j >= len(m[0]):
        return 0

    if m[i][j] != pv + 1:
        return 0

    if m[i][j] == 9:
        alreadyExists = (i, j) in s
        s.add((i, j))
        return 1 if not alreadyExists else 0
    
    cv = m[i][j]

    up = findPath(m, i - 1, j, s, cv)
    right = findPath(m, i, j + 1, s, cv)
    down = findPath(m, i + 1, j, s, cv)
    left = findPath(m, i, j - 1, s, cv)

    return up + right + down + left

def findPath2(m, i, j, s, pv):

    if i < 0 or i >= len(m) or j < 0 or j >= len(m[0]):
        return 0

    if m[i][j] != pv + 1:
        return 0

    if m[i][j] == 9:
        s.add((i, j))
        return 1
    
    cv = m[i][j]

    up = findPath2(m, i - 1, j, s, cv)
    right = findPath2(m, i, j + 1, s, cv)
    down = findPath2(m, i + 1, j, s, cv)
    left = findPath2(m, i, j - 1, s, cv)

    return up + right + down + left
    

def solve(data):
    
    trailheads = findTrailheads(data)

    s = 0

    for trailhead in trailheads:

        s += findPath(data, trailhead[0], trailhead[1], set(), -1)

    return s

def solve2(data):

    trailheads = findTrailheads(data)

    s = 0

    for trailhead in trailheads:

        s += findPath2(data, trailhead[0], trailhead[1], set(), -1)

    return s

def main():

    data = []
    
    with open(sys.argv[1]) as f:

        for line in f:

            data.append([int(n) for n in line.strip()])

    # result = solve(data)
    result = solve2(data)

    print(result)


###########################

if __name__ == "__main__":
    startTime = time.time()
    main()
    print(f'Runtime {time.time() - startTime} sec')
