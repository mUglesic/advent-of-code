
import sys
import time
import math

# RED GREEN BLUE
CONDITION = [12, 13, 14]

def solve(data):

    possibleGames = 0
    
    for line in data:

        splitLine = line.split(": ")

        gameID = int(splitLine[0].split(" ")[-1])

        cubeSubsets = splitLine[1].split("; ")

        conditionMet = True

        for s in cubeSubsets:

            hand = s.split(", ")

            totalCubes = [0, 0, 0]

            for cubes in hand:

                cubeCount = int(cubes.split(" ")[0])
                cubeColor = cubes.split(" ")[1]

                match cubeColor:
                    case "red":
                        totalCubes[0] += cubeCount
                    case "green":
                        totalCubes[1] += cubeCount
                    case "blue":
                        totalCubes[2] += cubeCount
                    
            for i, color in enumerate(CONDITION):

                if totalCubes[i] > color:
                    conditionMet = False
                    break
            
            if not conditionMet:
                break
            
        if conditionMet:
            # print(line)
            possibleGames += gameID

    return possibleGames

def solve2(data):

    powerTotal = 0
    
    for line in data:

        splitLine = line.split(": ")

        gameID = int(splitLine[0].split(" ")[-1])

        cubeSubsets = splitLine[1].split("; ")

        minCubes = [0, 0, 0]

        for s in cubeSubsets:

            hand = s.split(", ")

            totalCubes = [0, 0, 0]

            for cubes in hand:

                cubeCount = int(cubes.split(" ")[0])
                cubeColor = cubes.split(" ")[1]

                match cubeColor:
                    case "red":
                        totalCubes[0] += cubeCount
                    case "green":
                        totalCubes[1] += cubeCount
                    case "blue":
                        totalCubes[2] += cubeCount
            
            for i, count in enumerate(minCubes):
                minCubes[i] = max(count, totalCubes[i])
        
        powerTotal += math.prod(minCubes)

    return powerTotal

def main():

    data = []
    
    with open(sys.argv[1]) as f:

        for line in f:

            data.append(line.strip())

    # result = solve(data)
    result = solve2(data)

    print(result)


###########################

if __name__ == "__main__":
    startTime = time.time()
    main()
    print(f'Runtime {time.time() - startTime} sec')
