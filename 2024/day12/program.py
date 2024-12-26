
import sys
import time

def mapRegion(f, rm, r, i, j, p, rn):

    if i < 0 or i >= len(f) or j < 0 or j >= len(f[0]):
        return 0

    if f[i][j] != p:
        return 0

    if rm[i][j] != -1:
        return 0

    rm[i][j] = rn
    if len(r) == rn:
        r.append([])
    r[rn].append((i, j))

    up = mapRegion(f, rm, r, i - 1, j, p, rn)
    right = mapRegion(f, rm, r, i, j + 1, p, rn)
    down = mapRegion(f, rm, r, i + 1, j, p, rn)
    left = mapRegion(f, rm, r, i, j - 1, p, rn)

def calculatePerimeter(farm, region, plot):

    s = 0

    for plant in region:

        i, j = plant

        up = 1 if i - 1 < 0 or farm[i - 1][j] != plot else 0
        right = 1 if j + 1 >= len(farm[0]) or farm[i][j + 1] != plot else 0
        down = 1 if i + 1 >= len(farm) or farm[i + 1][j] != plot else 0
        left = 1 if j - 1 < 0 or farm[i][j - 1] != plot else 0

        s += up + right + down + left

    return s

def solve(data):

    farm = data
    regionMap = [[-1 for plot in row] for row in farm]
    regions = []

    regionNum = 0

    for i, row in enumerate(farm):
        for j, plot in enumerate(row):

            if regionMap[i][j] == -1:

                mapRegion(farm, regionMap, regions, i, j, plot, regionNum)

                regionNum += 1

    # for line in regionMap:
    #     print(*line)
    # print(regions)

    s = 0

    for i, region in enumerate(regions):

        s += len(region) * calculatePerimeter(regionMap, region, i)

    return s

def main():

    data = []
    
    with open(sys.argv[1]) as f:

        for line in f:

            data.append(list(line.strip()))

    result = solve(data)

    print(result)


###########################

if __name__ == "__main__":
    startTime = time.time()
    main()
    print(f'Runtime {time.time() - startTime} sec')
