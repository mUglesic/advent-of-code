
import sys
import time
from math import lcm

def findMap(name, maps):

    for map in maps:
        if map["name"] == name:
            return map
    
    return None

def solve(data):

    instructions = data[0]

    maps = []

    for map in data[2:]:
        
        name, lr = map.split(" = ")

        left, right = lr[1:-1].split(", ")

        maps.append({
            "name": name,
            "left": left,
            "right": right
        })

    foundEnd = False
    currentMap = findMap("AAA", maps)
    steps = 0

    while not foundEnd:

        for c in instructions:

            match c:
                case "L":
                    currentMap = findMap(currentMap["left"], maps)
                case "R":
                    currentMap = findMap(currentMap["right"], maps)

            steps += 1
            
            if currentMap["name"] == "ZZZ":
                foundEnd = True
                break

    return steps

def findStartingMaps(maps):

    ms = []

    for map in maps:
        if map["name"][-1] == "A":
            ms.append(map)

    return ms

def solve2(data):

    instructions = data[0]

    maps = []

    for map in data[2:]:
        
        name, lr = map.split(" = ")

        left, right = lr[1:-1].split(", ")

        maps.append({
            "name": name,
            "left": left,
            "right": right
        })

    currentMaps = findStartingMaps(maps)
    steps = 0
    allSteps = []

    while currentMaps:

        for c in instructions:

            # print(steps, currentMaps)

            for i, currentMap in enumerate(currentMaps):
                match c:
                    case "L":
                        currentMaps[i] = findMap(currentMap["left"], maps)
                    case "R":
                        currentMaps[i] = findMap(currentMap["right"], maps)

            steps += 1

            for map in currentMaps:
                if map["name"][-1] == "Z":
                    currentMaps.remove(map)
                    allSteps.append(steps)

    return lcm(*allSteps)

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
