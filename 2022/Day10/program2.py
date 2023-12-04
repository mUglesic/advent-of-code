
import sys

def solve(data):

    x = 1
    cycleCount = 1

    for line in data:
        print('#' if cycleCount >= x - 1 and cycleCount <= x + 1 else '.', end='')

        cycleCount += 1

        cycleCount %= 40

        if cycleCount == 0: print()

        if line == 'noop':
            pass
        else:
            val = int(line.split(' ')[1])

            x += val

            print('#' if cycleCount >= x - 1 and cycleCount <= x + 1 else '.', end='')

            cycleCount += 1

            cycleCount %= 40

            if cycleCount == 0: print()

def main():

    data = []
    
    with open(sys.argv[1]) as f:

        for line in f:

            data.append(line.strip())

    # result = solve(data)
    solve(data)

    # print(result)


###########################

if __name__ == "__main__":
    main()