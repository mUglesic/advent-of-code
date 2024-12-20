
import sys
import time
import math

def checkSolvable(result, nums, i, currentResult):

    if currentResult == result:
        return True
    
    if i >= len(nums) or currentResult > result:
        return False

    return checkSolvable(result, nums, i + 1, currentResult + nums[i]) or checkSolvable(result, nums, i + 1, currentResult * nums[i])

def solve(data):

    eqs = []

    for line in data:

        testVal, nums = line.split(": ")
        eq = {
            "tv": int(testVal),
            "ns": [int(n) for n in nums.split(" ")],
            "solvable": False
        }

        eqs.append(eq)

    s = 0

    for eq in eqs:

        eq["solvable"] = checkSolvable(eq["tv"], eq["ns"][1:], 0, eq["ns"][0])
        s += eq["tv"] if eq["solvable"] else 0

    return s

def intConcat(a, b):

    return int(a * 10**(1 + math.floor(math.log10(b))) + b)

def checkSolvableConcat(result, nums, i, currentResult):

    if currentResult == result and i == len(nums):
        return True
    
    if i >= len(nums) or currentResult > result:
        return False

    return checkSolvableConcat(result, nums, i + 1, currentResult + nums[i]) or checkSolvableConcat(result, nums, i + 1, currentResult * nums[i]) or checkSolvableConcat(result, nums, i + 1, intConcat(currentResult, nums[i]))

def solve2(data):

    eqs = []

    for line in data:

        testVal, nums = line.split(": ")
        eq = {
            "tv": int(testVal),
            "ns": [int(n) for n in nums.split(" ")],
            "solvable": False
        }

        eqs.append(eq)

    s = 0

    for eq in eqs:

        eq["solvable"] = checkSolvableConcat(eq["tv"], eq["ns"][1:], 0, eq["ns"][0])
        s += eq["tv"] if eq["solvable"] else 0

    return s

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
