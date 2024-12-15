
import sys
import time

from functools import reduce

def solve1(data):

    left, right = [], []
    
    for line in data:

        splitLine = line.split("   ")
        left.append(int(splitLine[0]))
        right.append(int(splitLine[1]))

    left.sort()
    right.sort()

    return reduce(lambda x, y: x + y, [abs(left[i] - right[i]) for i in range(len(left))])

def solve2(data):

    left, right = [], {}
    sum = 0
    
    for line in data:

        splitLine = [int(n) for n in line.split("   ")]
        left.append(splitLine[0])
        right[splitLine[1]] = 1 if not splitLine[1] in right else right[splitLine[1]] + 1

    for num in left:

        sum += (right[num] * num) if num in right else 0

    return sum

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
