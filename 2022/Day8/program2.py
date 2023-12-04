
import sys

def checkHorizontal(data, i, j):

    val = data[i][j]
    leftCounter = 0
    rightCounter = 0

    for x in range(j - 1, -1, -1):
        if val <= data[i][x]: leftCounter += 1; break
        leftCounter += 1

    for x in range(j + 1, len(data[i])):
        if val <= data[i][x]: rightCounter += 1; break
        rightCounter += 1

    # print(val, leftCounter, rightCounter)

    return leftCounter * rightCounter

def checkVertical(data, i, j):

    val = data[i][j]
    topCounter = 0
    bottomCounter = 0

    for y in range(i - 1, -1, -1):
        if val <= data[y][j]: topCounter += 1; break
        topCounter += 1

    for y in range(i + 1, len(data)):
        if val <= data[y][j]: bottomCounter += 1; break
        bottomCounter += 1
    
    # print(val, topCounter, bottomCounter)

    return topCounter * bottomCounter

def solve(data):

    max = 0

    for i in range(0, len(data)):
        for j in range(0, len(data[i])):
            
            current = checkHorizontal(data, i, j) * checkVertical(data, i, j)

            if current > max: max = current

    return max

def main():

    data = []
    
    with open(sys.argv[1]) as f:

        for line in f:

            data.append(list(map(lambda x: int(x), line.strip())))

    result = solve(data)

    print(result)


###########################

if __name__ == "__main__":
    main()