
import sys
import time

def findEdges(rocks):

    minX = 600
    maxX = 0

    maxY = 0

    for line in rocks:
        for x,y in line:
            if x < minX: minX = x
            if x > maxX: maxX = x
            if y > maxY: maxY = y

    return (minX, maxX, 0, maxY)

def createCave(w, h, off, rocks):

    cave = [['.' for j in range(w)] for i in range(h)]

    for line in rocks:
        for i in range(len(line) - 1):

            startX, startY = line[i]
            endX, endY = line[i + 1]

            # print(startX, startY, endX, endY)

            stepX = 1 if endX > startX else -1
            stepY = 1 if endY > startY else -1

            if startY == endY:
                for x in range(startX, endX + stepX, stepX):
                    cave[startY][x - off] = '#'

            if startX == endX:
                for y in range(startY, endY + stepY, stepY):
                    cave[y][startX - off] = '#'

    for x in range(w):
        cave[h - 1][x] = '#'

    cave[0][500 - off] = '+'

    return (cave, (500 - off, 0))

def runSim(cave, sandStart):

    h = len(cave)
    w = len(cave[0])

    sandX, sandY = sandStart

    counter = 0
    finish = False

    while True:

        if cave[sandY][sandX] == 'o': break

        newSandX, newSandY = sandX, sandY

        for t in range(h):

            downY = newSandY + 1
            leftX = newSandX - 1
            rightX = newSandX + 1

            if downY >= h:
                finish = True
                break

            if cave[downY][newSandX] == '.':
                newSandY += 1
            elif cave[downY][leftX] == '.':
                newSandY += 1
                newSandX -= 1
            elif cave[downY][rightX] == '.':
                newSandY += 1
                newSandX += 1
            else:
                cave[newSandY][newSandX] = 'o'
                counter += 1
                break

        if finish: break

    return counter

def printCave(cave):

    for line in cave:
        for spot in line:
            print(spot, end='')
        print()

def solve(data):

    rocks = []

    for line in data:

        coords = line.split(' -> ')
        coords = list(map(lambda x: (int(x.split(',')[0]), int(x.split(',')[1])), coords))

        rocks.append(coords)

    minX, maxX, minY, maxY = findEdges(rocks)

    width = maxX - minX + 1
    height = maxY - minY + 1
    # height = 500
    offset = minX

    cave, sandStart = createCave(width + (2 * height), height + 2, offset - height, rocks)

    # print(width + (2 * height), height + 2)

    # print(*cave, sep='\n')

    # printCave(cave)

    sandCount = runSim(cave, sandStart)

    # printCave(cave)

    return sandCount

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
    print('Runtime: %s sec' % (time.time() - startTime))