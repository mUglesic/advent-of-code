
import sys
import time

def solve(data):

    stones = [int(n) for n in data[0].split(" ")]

    for i in range(25):

        newStones = []

        for stone in stones:

            stoneStr = str(stone)
            stoneStrLen = len(stoneStr)

            if stone == 0:
                newStones.append(1)
            elif stoneStrLen % 2 == 0:
                newStones.extend([int(n) for n in [stoneStr[:int(stoneStrLen/2)], stoneStr[int(stoneStrLen/2):]]])
            else:
                newStones.append(stone * 2024)
        
        stones = newStones
    
    return len(stones)

def main():

    data = []
    
    with open(sys.argv[1]) as f:

        for line in f:

            data.append(line.strip())

    result = solve(data)

    print(result)


###########################

if __name__ == "__main__":
    startTime = time.time()
    main()
    print(f'Runtime {time.time() - startTime} sec')
