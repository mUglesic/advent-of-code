
import sys

def checkHorizontal(data, i, j):

    val = data[i][j]
    fromLeft = True
    fromRight = True

    for x in range(0, j):
        if val <= data[i][x]: fromLeft = False; break

    for x in range(j + 1, len(data[i])):
        if val <= data[i][x]: fromRight = False; break

    return fromLeft or fromRight

def checkVertical(data, i, j):

    val = data[i][j]
    fromTop = True
    fromBottom = True

    for y in range(0, i):
        if val <= data[y][j]: fromTop = False; break

    for y in range(i + 1, len(data)):
        if val <= data[y][j]: fromBottom = False; break

    return fromTop or fromBottom

def solve(data):

    counter = 0

    for i in range(0, len(data)):
        for j in range(0, len(data[i])):
            
            counter += 1 if checkHorizontal(data, i, j) or checkVertical(data, i, j) else 0

    return counter

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