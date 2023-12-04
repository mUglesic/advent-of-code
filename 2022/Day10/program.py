
import sys

def solve(data):

    x = 1
    cycleCount = 1
    sum = 0

    for line in data:

        if line == 'noop':
            cycleCount += 1
        else:
            val = int(line.split(' ')[1])

            cycleCount += 1

            if (cycleCount - 20) % 40 == 0:
                # print(cycleCount, x)
                sum += (cycleCount * x)

            x += val

            cycleCount += 1

        # print(x)

        if (cycleCount - 20) % 40 == 0:
            # print(cycleCount, x)
            sum += (cycleCount * x)

    return sum

def main():

    data = []
    
    with open(sys.argv[1]) as f:

        for line in f:

            data.append(line.strip())

    result = solve(data)

    print(result)


###########################

if __name__ == "__main__":
    main()