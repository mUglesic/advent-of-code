
import sys

def findStart(data):
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            if char == 'S': return (i, j)

def findStarts(data):
    
    starts = []

    for i, line in enumerate(data):
        for j, char in enumerate(line):
            if char == 'S' or char == 'a': starts.append((i, j))
    
    return starts

def findNeighbors(i, j, h, w):

    ns = []

    for iN, jN in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
        if 0 <= iN < h and 0 <= jN < w:
            ns.append((iN, jN))

    return ns

def isLower(c1, c2):
    return (ord(c2.replace('E', 'z')) <= ord(c1.replace('S', 'a')) + 1)

def solve(data):

    height = len(data)
    width = len(data[0])

    q = []
    visited = set()

    # Part One

    # start = findStart(data)

    # q.append((0, start[0], start[1]))

    # Part two

    starts = findStarts(data)

    for i, j in starts: q.append((0, i, j))

    for length, i, j in q:

        if data[i][j] == 'E':
            return length

        for iN, jN in findNeighbors(i, j, height, width):
            if isLower(data[i][j], data[iN][jN]) and (iN, jN) not in visited:
                visited.add((iN, jN))
                q.append((length + 1, iN, jN))

    return -1

def main():

    data = []
    
    with open(sys.argv[1]) as f:

        for line in f:

            data.append(list(line.strip()))

    result = solve(data)

    print(result)


###########################

if __name__ == "__main__":
    main()