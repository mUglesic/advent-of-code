
import sys
import time
import copy

def findStart(data):

    for i, line in enumerate(data):
        for j, c in enumerate(line):

            if c == "^":
                return i, j
            
def checkBounds(i, j, height, width):

    return i >= 0 and i < height and j >= 0 and j < width

def turnRight(dir):

    match dir:
        case (-1, 0):
            return (0, 1)
        case (0, 1):
            return (1, 0)
        case (1, 0):
            return (0, -1)
        case (0, -1):
            return (-1, 0)

def solve(data):

    height = len(data)
    width = len(data[0])

    visited = [["." for _ in line] for line in data]

    i, j = findStart(data)
    dir = (-1, 0)
    visited[i][j] = "X"

    count = 1

    while checkBounds(i + dir[0], j + dir[1], height, width):

        if data[i + dir[0]][j + dir[1]] == "#":
            dir = turnRight(dir)
        else:
            i, j = i + dir[0], j + dir[1]
            if visited[i][j] != "X":
                count += 1
                visited[i][j] = "X"

    return count, visited

def createOptions(data):

    _, visited = solve(data)

    options = []

    for i, line in enumerate(data):
        for j, space in enumerate(line):

            if space == "." and visited[i][j] == "X":
                dataCopy = copy.deepcopy(data)
                dataCopy[i][j] = "#"
                options.append(dataCopy)
    
    return options

def solve2(data):

    height = len(data)
    width = len(data[0])

    iStart, jStart = findStart(data)

    count = 0

    for index, option in enumerate(createOptions(data)):

        # print(index)

        visited = [[{"field": ".", "dir": []} for _ in line] for line in option]

        i, j = iStart, jStart

        dir = (-1, 0)
        visited[i][j]["field"] = "X"
        visited[i][j]["dir"].append(dir)

        while checkBounds(i + dir[0], j + dir[1], height, width):

            if option[i + dir[0]][j + dir[1]] == "#":
                dir = turnRight(dir)
            else:
                i, j = i + dir[0], j + dir[1]

                if visited[i][j]["field"] == "X" and dir in visited[i][j]["dir"]:
                    count += 1
                    break

                visited[i][j]["field"] = "X"
                visited[i][j]["dir"].append(dir)

    return count

def main():

    data = []
    
    with open(sys.argv[1]) as f:

        for line in f:

            data.append(list(line.strip()))

    # result = solve(data)[0]
    result = solve2(data)

    print(result)


###########################

if __name__ == "__main__":
    startTime = time.time()
    main()
    print(f'Runtime {time.time() - startTime} sec')
