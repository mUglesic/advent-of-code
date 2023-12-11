
import sys
import time

def printUniverse(universe):

    for row in universe:

        for space in row:

            print(space,end="")

        print()

def largerThan(n, arr):

    count = 0

    for a in arr:
        if n > a:
            count += 1
    
    return count

def dimsAdded(universe):

    rowsAdded = []

    for i, row in enumerate(universe):

        allEmpty = True

        for space in row:
            if space != ".":
                allEmpty = False
                break

        if allEmpty:
            rowsAdded.append(i)

    colsAdded = []

    for i in range(len(universe[0])):

        allEmpty = True

        for row in universe:
            if row[i] != ".":
                allEmpty = False
                break
        
        if allEmpty:
            colsAdded.append(i)

    return (rowsAdded, colsAdded)

def expandedManhattanDistances(universe, rows, cols, expandBy):

    galaxies = []
    distances = []

    for i, row in enumerate(universe):
        for j, space in enumerate(row):
            if space == "#":
                galaxies.append((i + largerThan(i, rows) * expandBy, j + largerThan(j, cols) * expandBy))

    pairs = set()

    for galaxy in galaxies:

        others = galaxies.copy()
        others.remove(galaxy)

        for other in others:

            pairs.add(tuple(sorted((galaxy, other))))

    for galaxy, other in pairs:

        x1, y1 = galaxy
        x2, y2 = other

        distances.append(abs(x1 - x2) + abs(y1 - y2))

    return distances

def solve(universe, expandBy):

    rowsAdded, colsAdded = dimsAdded(universe)

    distances = expandedManhattanDistances(universe, rowsAdded, colsAdded, expandBy)

    return sum(distances)

def main():

    data = []
    
    with open(sys.argv[1]) as f:

        for line in f:

            data.append(list(line.strip()))

    result = solve(data, 1)
    result2 = solve(data, 999_999)

    print(result, result2)


###########################

if __name__ == "__main__":
    startTime = time.time()
    main()
    print(f'Runtime {time.time() - startTime} sec')
