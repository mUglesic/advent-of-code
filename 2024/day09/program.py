
import sys
import time
import copy

def solve(data):

    diskMap = []

    currentNum = 0
    write = True

    for n in data[0]:
        if write:
            for i in range(n):
                diskMap.append(currentNum)
            write = False
            currentNum += 1
        else:
            for i in range(n):
                diskMap.append('.')
            write = True

    iReplace = 0

    for i in range(len(diskMap) - 1, -1, -1):

        while i > 0 and diskMap[i] == '.':
            i -= 1

        while iReplace < len(diskMap) and diskMap[iReplace] != '.':
            iReplace += 1

        if iReplace >= len(diskMap) or iReplace >= i:
            break
        
        diskMap[iReplace] = diskMap[i]
        diskMap[i] = '.'
        iReplace += 1

    sum = 0

    for i, n in enumerate(diskMap):

        if n == ".": break
        
        sum += (i * n)

    return sum

def printDiskMap(diskMap):

    for file in diskMap:

        for i in range(file["size"]):
            print(file["value"], end="")

    print("\n----------------------------------------")

def findFirstPossibleSpot(diskMap, file, indexLimit):

    for i, f in enumerate(diskMap):

        if i >= indexLimit: return -1

        if f["value"] == '.' and f["size"] >= file["size"]:
            return i

    return -1

def insertIntoDiskMap(diskMap, file, iInsert):

    # print("Inserting file", file, "into diskMap at index", iInsert)

    sizeDif = diskMap[iInsert]["size"] - file["size"]

    iFix = diskMap.index(file)

    diskMap.pop(iFix)
    diskMap.insert(iFix, {"value": ".", "size": file["size"]})

    diskMap.pop(iInsert)
    diskMap.insert(iInsert, file)
    
    if sizeDif > 0:
        diskMap.insert(iInsert + 1, {"value": ".", "size": sizeDif})

def calculateChecksum(diskMap):

    index = 0
    s = 0

    for file in diskMap:

        if file["value"] != ".":
            for i in range(file["size"]):
                s += (index * file["value"])
                index += 1
        else:
            index += file["size"]
    
    return s

def solve2(data):

    diskMap = []

    write = True
    currentNum = 0

    for n in data[0]:
        
        if n != 0: diskMap.append({"value": currentNum if write else '.', "size": n})
        currentNum += 1 if write else 0
        write = not write

    # print("Start disk map: ", end="")
    # printDiskMap(diskMap)

    diskMapSorted = copy.deepcopy(diskMap)

    for i in range(len(diskMap) - 1, -1, -1):

        file = diskMap[i]

        if file["value"] == '.': continue

        # print("Current file:", file)

        toReplace = findFirstPossibleSpot(diskMapSorted, file, diskMapSorted.index(file))

        if toReplace > 0:
            # print("Found spot at index", toReplace)
            insertIntoDiskMap(diskMapSorted, file, toReplace)
            # printDiskMap(diskMapSorted)

    return calculateChecksum(diskMapSorted)

def main():

    data = []
    
    with open(sys.argv[1]) as f:

        for line in f:

            data.append([int(n) for n in line.strip()])

    # result = solve(data)
    result = solve2(data)

    print(result)


###########################

if __name__ == "__main__":
    startTime = time.time()
    main()
    print(f'Runtime {time.time() - startTime} sec')
