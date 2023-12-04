
import sys
import time

gears = []

def checkNeighbors(data, n):

    iStart = n["lineIndex"]
    jStart = n["startIndex"]
    jEnd = n["endIndex"]

    # print("checking ", n["s"])

    for i in range(iStart - 1, iStart + 2):

        for j in range(jStart, jEnd + 1):

            for neighbor in range(j - 1, j + 1):

                if i < 0 or i >= len(data) or neighbor < 0 or neighbor >= len(data[0]):
                    continue

                if data[i][neighbor] not in "0123456789.":

                    if data[i][neighbor] == "*":
                        
                        gear = findGear(i, neighbor)

                        if gear:
                            gear["adjacentNums"].append(int(n["s"]))
                        else:
                            gears.append({
                                "i": i,
                                "j": neighbor,
                                "adjacentNums": [int(n["s"])]
                            })

                    return True
                
    return False

def findGear(i, j):

    for gear in gears:
        if gear["i"] == i and gear["j"] == j:
            return gear

def solve(data):

    candidates = []
    partNums = []

    i, j = 0, 0

    while i < len(data):

        j = 0

        line = data[i]

        while j < len(line):

            char = line[j]

            if char in "0123456789":

                startIndex = j

                while j < len(line) and line[j] in "0123456789":

                    j += 1
                
                endIndex = j

                n = {
                    "lineIndex": i,
                    "startIndex": startIndex,
                    "endIndex": endIndex,
                    "s": line[startIndex:endIndex]
                }

                candidates.append(n)
            
            j += 1
        
        i += 1

    for candidate in candidates:

        if checkNeighbors(data, candidate):
            partNums.append(int(candidate["s"]))

    return sum(partNums)

def solve2():

    ratios = []

    for gear in gears:

        if len(gear["adjacentNums"]) == 2:
            ratios.append(gear["adjacentNums"][0] * gear["adjacentNums"][1])

    return sum(ratios)

def main():

    data = []
    
    with open(sys.argv[1]) as f:

        for line in f:

            data.append(line.strip())

    result = solve(data)

    result2 = solve2()

    print("Part one: ", result)
    print("Part Two: ", result2)


###########################

if __name__ == "__main__":
    startTime = time.time()
    main()
    print(f'Runtime {time.time() - startTime} sec')
