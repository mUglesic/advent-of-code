
import sys
import time

def allZeroes(l):

    for e in l:
        if e != 0:
            return False
    
    return True

def reduce(history):

    historyHistory = []
        
    while not allZeroes(history):

        historyHistory.append(history)

        newList = []

        for i in range(len(history) - 1):

            current, next = history[i], history[i + 1]

            newList.append(next - current)

        history = newList

    historyHistory.append(history)

    return historyHistory

def extrapolate(reduced):

    history = reduced[::-1]

    for i in range(1, len(history)):

        step = history[i]

        extrapolated = history[i - 1][-1] + step[-1]

        step.append(extrapolated)

    return history[-1][-1]


def solve(data):

    s = 0

    for line in data:

        history = [int(e) for e in line.split(" ")]

        reduced = reduce(history)

        extrapolated = extrapolate(reduced)

        s += extrapolated

    return s

def extrapolateBackwards(reduced):

    history = reduced[::-1]

    for i in range(1, len(history)):

        step = history[i]

        extrapolated = step[0] - history[i - 1][0]

        step.insert(0, extrapolated)

    return history[-1][0]

def solve2(data):

    s = 0

    for line in data:

        history = [int(e) for e in line.split(" ")]

        reduced = reduce(history)

        extrapolated = extrapolateBackwards(reduced)

        s += extrapolated

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
