
import sys
import time

def checkSafe(levels):

    safe = True
    increasing = levels[0] < levels[-1]

    for i in range(0, len(levels) - 1):

        curVal = levels[i]
        nextVal = levels[i + 1]

        safe = (increasing and nextVal > curVal and nextVal - curVal <= 3) or (not increasing and nextVal < curVal and curVal - nextVal <= 3)

        if not safe: return 0

    return 1

def solve1(data):

    safeCount = 0

    for line in data:

        levels = [int(n) for n in line.split(" ")]

        safeCount += checkSafe(levels)

    return safeCount

def solve2(data):

    safeCount = 0

    for line in data:

        levels = [int(n) for n in line.split(" ")]

        if checkSafe(levels) == 0:
            for i in range(len(levels)):
                if checkSafe(levels[:i] + levels[i + 1:]) == 1:
                    safeCount += 1
                    break
        else:
            safeCount += 1

    return safeCount

def main():

    data = []
    
    with open(sys.argv[1]) as f:

        for line in f:

            data.append(line.strip())

    # result = solve1(data)
    result = solve2(data)

    print(result)


###########################

if __name__ == "__main__":
    startTime = time.time()
    main()
    print(f'Runtime {time.time() - startTime} sec')
