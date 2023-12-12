
import sys
import time

from functools import cache

# def getGroups(springs):

#     groups = []
#     count = 0

#     for spring in springs:

#         if spring == ".":
#             if count > 0:
#                 groups.append(str(count))
#             count = 0
#         elif spring == "#":
#             count += 1
    
#     if count > 0:
#         groups.append(str(count))

#     return ",".join(groups)

@cache
def recSolve(springs, groups, groupSize):

    if not springs:
        return 1 if (len(groups) == 1 and groups[0] == groupSize) or (len(groups) == 0 and groupSize == 0) else 0
    
    spring = springs[0]
    springs = springs[1:]

    group, *newGroups = groups or [0]

    newGroups = tuple(newGroups)
    
    if spring == "?":

        return recSolve("#" + springs, groups, groupSize) + recSolve("." + springs, groups, groupSize)
    
    elif spring == "#":

        return 0 if groupSize > group else recSolve(springs, groups, groupSize + 1)
    
    elif spring == ".":

        if groupSize == 0:
            return recSolve(springs, groups, 0)
        elif groupSize == group:
            return recSolve(springs, newGroups, 0)
        
        return 0

def solve(data):

    count = 0

    for line in data:

        springs, groups = line.split(" ")

        groups = tuple(map(int, groups.split(",")))

        # print(springs)

        # print(springs, groups, "|", getGroups(springs))

        count += recSolve(springs, groups, 0)

        # print(count)

    return count

def solve2(data):

    count = 0

    for line in data:

        springs, groups = line.split(" ")

        springs = "?".join([springs] * 5)
        groups = tuple(map(int, ",".join([groups] * 5).split(",")))

        # print(springs)

        # print(springs, groups, "|", getGroups(springs))

        count += recSolve(springs, groups, 0)

        # print(count)

    return count

def main():

    data = []
    
    with open(sys.argv[1]) as f:

        for line in f:

            data.append(line.strip())

    result = solve(data)
    result2 = solve2(data)

    print(result, result2)


###########################

if __name__ == "__main__":
    startTime = time.time()
    main()
    print(f'Runtime {time.time() - startTime} sec')
