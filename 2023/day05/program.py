
import sys
import time

def createMaps(data):

    maps = []

    i = 3
    iMap = 0

    while i < len(data):

        line = data[i]

        maps.append([])

        while True:

            line = data[i]

            if line == "":
                break

            [destStart, srcStart, rangeLength] = line.split(" ")

            maps[iMap].append({
                "destStart": int(destStart),
                "srcStart": int(srcStart),
                "rangeLength": int(rangeLength)
            })

            i += 1

            if i >= len(data):
                break

        iMap += 1
        i += 2
    
    return maps


def checkMap(r, m):

    if r >= m["srcStart"] and r < m["srcStart"] + m["rangeLength"]:

        return m["destStart"] + r - m["srcStart"]
    
    return r

def solve(data):

    seeds = data[0].split(": ")[1].split(" ")

    maps = createMaps(data)

    locations = []

    for seed in seeds:

        r = int(seed)

        for map in maps:

            for m in map:

                rOld = r
                r = checkMap(r, m)

                if r != rOld:
                    break
        
        locations.append(r)

    return min(locations)

def checkMap2(r, m):

    if r >= m["destStart"] and r < m["destStart"] + m["rangeLength"]:

        return m["srcStart"] + r - m["destStart"]
    
    return r

def verifyResult(r, seeds):

    for seed in seeds:

        if r >= seed["start"] and r < seed["start"] + seed["length"]:
            return True
        
    return False

def solve2(data):

    seedCombinations = data[0].split(": ")[1].split(" ")

    seeds = []

    for i in range(0, len(seedCombinations), 2):

        seeds.append({"start": int(seedCombinations[i]), "length": int(seedCombinations[i + 1])})

    maps = createMaps(data)
    maps.reverse()

    percent = 0

    for i in range(100_000_000, 200_000_000):

        if i % 1_000_000 == 0:
            print(percent, "%")
            percent += 1

        r = i
        location = r
        
        for map in maps:

            for m in map:

                rOld = r
                r = checkMap2(r, m)

                if rOld != r:
                    break
        
        if verifyResult(r, seeds):
            return location
    
    return -1

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
