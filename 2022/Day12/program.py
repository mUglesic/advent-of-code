
import sys

def findStart(data):
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            if char == 'S':
                return {"x": j, "y": i}

def shortestPath(pos, length, data, visited, prev):

    if not (pos["y"] >= 0 and pos["y"] < len(data) and pos["x"] >= 0 and pos["x"] < len(data[pos["y"]])):
        return sys.maxsize

    if visited[pos["y"]][pos["x"]] != 0:
        return sys.maxsize

    if data[pos["y"]][pos["x"]] == 'E': 
        # print(length)
        return length

    if ord(prev) + 1 < ord(data[pos["y"]][pos["x"]]) and prev != 'S': 
        # print(prev, data[pos["y"]][pos["x"]])
        return sys.maxsize


    visited[pos["y"]][pos["x"]] = 1


    left = shortestPath({"x": pos["x"] - 1, "y": pos["y"]}, length + 1, data, visited, data[pos["y"]][pos["x"]])
    right = shortestPath({"x": pos["x"] + 1, "y": pos["y"]}, length + 1, data, visited, data[pos["y"]][pos["x"]])
    up = shortestPath({"x": pos["x"], "y": pos["y"] - 1}, length + 1, data, visited, data[pos["y"]][pos["x"]])
    down = shortestPath({"x": pos["x"], "y": pos["y"] + 1}, length + 1, data, visited, data[pos["y"]][pos["x"]])

    return min(left, right, up, down)

def solve(data, visited):

    start = findStart(data)

    return shortestPath(start, 0, data, visited, 'S')

def main():

    data = []
    visited = []
    
    with open(sys.argv[1]) as f:

        for line in f:

            data.append(list(line.strip()))
            visited.append(list(map(lambda x: 0, line.strip())))

    result = solve(data, visited)

    print(result)


###########################

if __name__ == "__main__":
    main()