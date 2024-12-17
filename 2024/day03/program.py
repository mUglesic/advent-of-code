
import sys
import time
import re

def solve(data):
    
    sum = 0

    for line in data:
    
        substrings = re.findall(r'mul\(\d+,\d+\)', line)

        for s in substrings:
            n = [int(x) for x in re.findall(r'\d+', s)]
            sum += (n[0] * n[1])
    
    return sum

def solve2(data):

    sum = 0
    count = True

    for line in data:

        substrings = re.findall(r"mul\(\d+,\d+\)|do(?:n't)?\(\)", line)

        for s in substrings:

            if s == "do()":
                count = True
            elif s == "don't()":
                count = False
            else:
                n = [int(x) for x in re.findall(r'\d+', s)]
                sum += (n[0] * n[1]) if count else 0
            
    return sum

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
