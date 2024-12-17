
import sys
import time

def checkXMAS(i, j, data):

    height = len(data)
    width = len(data[0])

    count = 0

    for y in range(-1, 2):
        for x in range(-1, 2):

            if x == 0 and y == 0: continue
            # print(x, y)

            yLimit, xLimit = i + (y * 3), j + (x * 3)

            if yLimit >= 0 and yLimit < height and xLimit >= 0 and xLimit < width:
                if data[i + (y * 1)][j + (x * 1)] == "M" and data[i + (y * 2)][j + (x * 2)] == "A" and data[i + (y * 3)][j + (x * 3)] == "S":
                    count += 1
                    # print(f"x: {j} | y: {i} | dir: {x}, {y}")

    return count

def solve1(data):

    count = 0

    for i, line in enumerate(data):

        for j, c in enumerate(line):

            if c == "X":
                count += checkXMAS(i, j, data)

    return count

def checkMAS(i, j, data):

    height = len(data)
    width = len(data[0])

    if i == 0 or i == height - 1 or j == 0 or j == width - 1: return 0

    count = 0

    if (data[i - 1][j - 1] == "M" and data[i + 1][j + 1] == "S") or (data[i - 1][j - 1] == "S" and data[i + 1][j + 1] == "M"):
        if (data[i - 1][j + 1] == "M" and data[i + 1][j - 1] == "S") or (data[i - 1][j + 1] == "S" and data[i + 1][j - 1] == "M"):
            count += 1

    return count

def solve2(data):

    count = 0

    for i, line in enumerate(data):

        for j, c in enumerate(line):

            if c == "A":
                count += checkMAS(i, j, data)

    return count

def main():

    data = []
    
    with open(sys.argv[1]) as f:

        for line in f:

            data.append(list(line.strip()))

    # result = solve1(data)
    result = solve2(data)

    print(result)


###########################

if __name__ == "__main__":
    startTime = time.time()
    main()
    print(f'Runtime {time.time() - startTime} sec')
